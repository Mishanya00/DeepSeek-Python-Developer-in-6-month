from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


# These dependencies will be executed/solved the same way as normal dependencies.
# But their value (if they return any) won't be passed to your path operation function.
# So, you can reuse a normal dependency (that returns a value) you already use somewhere else,
# and even though the value won't be used, the dependency will be executed

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]