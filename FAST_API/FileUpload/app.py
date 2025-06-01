import os
import shutil
from fastapi import FastAPI, File, UploadFile

# @router.post("/user")
# async def create_user(user: UserBase, db: db_dependency, image: UploadFile = File(...)):
#     UPLOAD_DIR = "static/pics"
#     os.makedir(UPLOAD_DIR, exist_ok=True)

#     img_path = os.path.join(UPLOAD_DIR, image.filename)
#     with open(img_path, "wb") as buffer:
#         shutil.copyfileobj(image.file, buffer)

app = FastAPI()

@app.post("/upload-file")
def upload_file(file: UploadFile=File(...)):
    upload_dir = "pics"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)
    try:
        with open(file_path, "wb") as buf:
            shutil.copyfileobj(file.file, buf)

        print("successfully")
        return {"file location": file_path}
    except Exception as e:
        print(e)
        return {"Error": str(e)}
