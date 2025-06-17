from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from app.leak_table import save_leak, get_all_leaks
from app.s3_upload import upload_media

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/leaks")
async def drop_leak(description: str = Form(...), type: str = Form("text"), file: UploadFile):
    media_url = upload_media(file) if file else None
    leak = save_leak(description, media_url, type)
    return {"message": "leak dropped", "leak": leak}

@app.get("/leaks")
def homepage_leaks():
    return {"leaks": get_all_leaks()}