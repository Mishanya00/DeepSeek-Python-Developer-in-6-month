from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html


# emulate database
users = {
    "Alex@mail.ru": "12345678",
    "Bob@gmail.com": "qwerty1234567890",
    "S1gma_3ncap5u1at3d@proton.me": "ALte1349d@495#",
}

EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom route to docs"""
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get("/users/")
async def get_users():
    return users


@app.get("/get_user/")
async def get_user(username: Annotated[str, Query(pattern=EMAIL_PATTERN)]):
    user = {username: users[username]}
    with open('temp.txt', 'w') as f:
        f.write(username + users[username])
    return user


@app.post("/register/")
async def register_user(
    username: Annotated[str, Query(pattern=EMAIL_PATTERN)],
    password: Annotated[str, Query(min_length=8)],
):
    users[username] = password
