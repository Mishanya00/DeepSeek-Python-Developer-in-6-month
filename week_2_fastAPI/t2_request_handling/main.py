from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    '''Custom route to docs'''
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, querry: str):
    return {"item_id": item_id, "querry": querry} 