from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os

app = FastAPI()


class Document(BaseModel):
    name: str
    content: bytes


@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed")

    contents = await file.read()
    document = Document(name=file.filename, content=contents)

    # Save the document to a specific directory
    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(contents)

    return JSONResponse(
        content={"message": "Document uploaded successfully"}, status_code=201
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(content={"error": "Internal server error"}, status_code=500)
