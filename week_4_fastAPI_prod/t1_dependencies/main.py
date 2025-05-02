from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


fake_db_users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 41},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 35},
    {"name": "Jona", "age": 29},
    {"name": "Kevin", "age": 45},
    {"name": "Laura", "age": 31},
    {"name": "Mike", "age": 38},
    {"name": "Nancy", "age": 26}
]


def api_key(key: Annotated[str, Header(min_length=32)]):
        if key != 'secret_key_of_length_at_least_32_chars_haha_98kdl2m42l':
            raise HTTPException(status_code=400, detail="API key is invalid!")        
        return key


class UserFilter:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit


@app.get('/')
async def hello():
    return {"message": "Hello!"}


@app.get('/users', dependencies=[Depends(api_key)])
async def get_users(filter: Annotated[UserFilter, Depends()]):
    filtered_users = fake_db_users[filter.skip:filter.skip+filter.limit]
    return filtered_users