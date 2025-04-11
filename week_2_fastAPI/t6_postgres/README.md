## Days 6-7: PostgreSQL with FastAPI

**Topics:**

- Raw SQL queries (asyncpg)
- SQLAlchemy ORM setup
- Connection pooling

**Tasks:**

1. Raw SQL Implementation
- Create 1 endpoint using asyncpg that:
  - `GET /products`: Returns all rows from a products table
2. SQLAlchemy Implementation
- Set up SQLAlchemy models for products
- Create 1 endpoint that:
  - `POST /products`: Adds new product using ORM
3. Connection Health Check
- Add `/health` endpoint that verifies database connectivity

(Optional)
4. 🐳 Dockerize (only if comfortable)

- Add PostgreSQL container in `docker-compose.yml`