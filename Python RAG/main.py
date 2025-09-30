from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from fastapi import FastAPI, Query
from pydantic import BaseModel

from vector import (
    add_to_chroma,
    get_embedding_function,
    load_documents,
    spilt_documents,
    clear_database,
)


class LLMResponse(BaseModel):
    prompt: str
    response: str
    formatted_response: str


app = FastAPI(title="RAG Query API", description="An API to query a RAG model.")


@app.get("/chat_with_llm", response_model=LLMResponse)
def query_rag(
    query_text: str = Query(description="The question you want to ask the RAG model."),
):
    vector_store = Chroma(
        persist_directory="chroma_langchain_db",
        embedding_function=get_embedding_function(),
    )

    PROMPT_TEMPLATE = """
        Anser the question based only on the following context:
        {context}

        ---
        Answer the question based on the above context: {question}
    """

    results = vector_store.similarity_search_with_score(query=query_text, k=7)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    print("=" * 55)
    print(prompt)
    print("=" * 55)

    model = OllamaLLM(model="phi4:14b")
    response = model.invoke(prompt)
    print("=" * 55)
    print(response)
    print("=" * 55)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response}\nSource: {sources}"
    print("=" * 55)
    print(formatted_response)
    print("=" * 55)

    return LLMResponse(
        prompt=prompt, response=response, formatted_response=formatted_response
    )


@app.post("/load_documents")
def load_vector_store():
    documents = load_documents()
    chunks = spilt_documents(documents)
    add_to_chroma(chunks)
    return {"message": "Done"}


@app.delete("/delete_vector_content")
def delete_vector_store():
    clear_database()
    return {"message": "Done"}
