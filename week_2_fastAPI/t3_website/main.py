from typing import Annotated

import chardet

from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"


@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# @app.get("/test")
# async def test_test(test_str: str):
#     return {"test": test_str}


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


@app.post("/uploadfile")
async def create_upload_file(file: Annotated[UploadFile | str, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    elif file.content_type != "text/plain":
        return {"message": "Not a text file!"}
    else:
        contents = await file.read()
        encoding = chardet.detect(contents)['encoding']
        print('TEXT ENCODING: ' + str(encoding))
        decoded = contents.decode(encoding or "utf-8", errors="replace")
        return {"filename": file.content_type, "contents": decoded}


# @app.post("/uploadfile/")
# async def create_upload_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}
