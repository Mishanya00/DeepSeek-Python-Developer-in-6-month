import time
import json

from fastapi import FastAPI, HTTPException
import redis


# You can check existing in real time data from redis via redis-cli
# To launch it run: docker exec -it redis redis-cli (in case of Docker redis container)
# Then type: KEYS *
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

app = FastAPI()


fake_db = {
    1: {"id": 1, "name": "Python Basics", "grade": "free"},
    2: {"id": 2, "name": "Advanced Python", "grade": "premium"},
    3: {"id": 3, "name": "FastAPI Pro", "grade": "premium"},
    4: {"id": 4, "name": "100k$ Crypto scam", "grade": "free"}
}


def get_course_from_db(course_id: int):
    """DB time consuming request imitation"""
    time.sleep(1)
    return fake_db.get(course_id)


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    cache_key = f"course:{course_id}"
    
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data)
    
    course = get_course_from_db(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Save to redis with TTL = 60 secs
    redis_client.setex(cache_key, 60, json.dumps(course))
    
    return course


@app.patch("/courses/{course_id}")
def update_course_grade(course_id: int, new_grade: str):
    if new_grade not in ["free", "premium"]:
        raise HTTPException(status_code=400, detail="Grade must be 'free' or 'premium'")
    
    if course_id not in fake_db:
        raise HTTPException(status_code=404, detail="Course not found")
    
    fake_db[course_id]["grade"] = new_grade
    
    cache_key = f"course:{course_id}"
    redis_client.delete(cache_key)
    
    return {"status": "updated", "course_id": course_id}