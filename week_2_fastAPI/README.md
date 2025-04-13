# FastAPI Intensive Learning Plan (1 Week)

## Prerequisites:

- Basic Flask knowledge (routes, templates)
- Python 3.7+ installed
- 3-4 hours daily commitment

---

## Day 1: FastAPI Fundamentals

**Topics:**

- FastAPI vs Flask comparison
- Basic route setup
- Automatic docs (Swagger/ReDoc)
- Path parameters

**Tasks:**

1. Install FastAPI: `pip install fastapi uvicorn`
2. Create a "Hello World" endpoint
3. Add 3 routes with different path params (`/items/1`, `/users/{name}`)
4. Explore auto-generated docs at `http://127.0.0.1:8000/docs`

---

## Day 2: Request Handling

**Topics:**

- Query parameters
- Request bodies (POST/PUT)
- Pydantic models
- Data validation

**Tasks:**

1. Create a POST endpoint for user registration
2. Validate:
   - Email format
   - Password length (min 8 chars)
3. Build a fake DB with list/dict storage
4. Add search with query params (`/users?username=test`)

---

## Day 3: Advanced Routing

**Topics:**

- Dependency injection
- Background tasks
- Form data handling
- File uploads

**Tasks:**

1. Create login form (username/password)
2. Implement file upload endpoint (.txt only)
3. Add task that cleans uploads after 1 hour
4. Build dependency for API key auth

---

## Day 4: Database Integration

**Topics:**

- SQLAlchemy setup
- Async database access
- CRUD operations
- Relationships

**Tasks:**

1. Setup SQLite with SQLAlchemy
2. Create User and Item models
3. Implement:
   - Create item
   - Get user's items
   - Delete item
4. Add pagination (limit/offset)

---

## Day 5: Authentication

**Topics:**

- JWT tokens
- OAuth2 with Password
- Security dependencies
- Cookie-based auth

**Tasks:**

1. Implement JWT token generation
2. Add protected route (requires auth)
3. Set up token refresh endpoint

---

## Days 6-7: PostgreSQL with FastAPI

**Topics:**

- Raw SQL queries (asyncpg or psycopg)

**Tasks:**

1. Raw SQL Implementation
- function to load config and to create connection
- function to create tables and insert into them
- function to update values

---

## Project to practice

**Final Project:**
Build a Bookstore API with:

(Separate repository & branch for this project: https://github.com/Mishanya00/Bookstore-FastAPI/tree/deepseek-task)

- [ ] User auth
- [ ] CRUD for books
- [ ] Search by title/author
- [ ] Purchase system
- [ ] Automated docs

**Bonus:**

- Add Redis caching
- Implement WebSocket notifications

---

## Resources:

- Official Docs: https://fastapi.tiangolo.com/
- Testing Guide: https://testdriven.io/blog/fastapi-crud/
- Deployment: https://fastapi.tiangolo.com/deployment/

> Pro Tip: Use `@app.get("/", response_model=...)` for automatic output validation!