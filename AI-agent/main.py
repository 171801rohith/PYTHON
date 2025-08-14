import re
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vectors import retriever

model = OllamaLLM(model="mistral")


def cleaned_response(result):
    return re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL)


template = """
    You are an expert in answering questions about pizza.

    Here are some relevent reviews: {reviews}

    Here is a question you need to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("=" * 75)
    question = input("Ask anything ... (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question) 
    result = chain.invoke({"reviews": reviews, "question": question})
    print(cleaned_response(result))
    print("=" * 75)
