from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

from pydantic import BaseModel


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    '''Custom route to docs'''
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get('/')
def read_root():
    '''Hello world endpoint'''
    return {"hello": "world"}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    '''Get item endpoint'''
    return {'item_id': item_id, "q": q}


@app.get('/users/{username}')
def hello_user(username: str):
    '''Get item endpoint'''
    return {'Hello': username}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}
