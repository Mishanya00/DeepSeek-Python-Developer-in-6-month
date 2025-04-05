from typing import Annotated

import os

import asyncio

import chardet

from fastapi import FastAPI, Request, Form, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"
UPLOAD_DIR = "file_storage"


if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def secure_filename(filename: str) -> str:
    return os.path.basename(filename).replace(" ", "_")  # Functionality may be extended


async def delete_user_file(filename: str, delay: int):
    await asyncio.sleep(delay)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass


@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def handle_login(
    request: Request,
    email: Annotated[str, Form(pattern=EMAIL_PATTERN)],
    password: Annotated[str, Form(min_length=8)],
):
    return RedirectResponse(url=f"/dashboard?email={email}", status_code=303)


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, email: str = None):
    if not email:
        return RedirectResponse(url="/")
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "user_email": email}
    )


# FastAPI will create the object of type BackgroundTasks and pass it as that parameter.
@app.post("/uploadfile")
async def create_upload_file(background_tasks: BackgroundTasks, file: Annotated[UploadFile | str, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    elif file.content_type != "text/plain":
        return {"message": "Not a text file!"}
    else:
        try:
            contents = await file.read()
            encoding = chardet.detect(contents)["encoding"]
            decoded = contents.decode(encoding or "utf-8", errors="replace")

            path = UPLOAD_DIR + "/" + secure_filename(file.filename)
            print(path)

            with open(path, "w", encoding="utf-8") as f:
                f.write(decoded)

            background_tasks.add_task(delete_user_file, path, 3600)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
        finally:
            await file.close()

        return {"message": f"file {file.filename} has been successfully uploaded."}
    