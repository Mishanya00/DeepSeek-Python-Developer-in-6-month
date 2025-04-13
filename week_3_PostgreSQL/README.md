# Week 3: PostgreSQL for Backend Devs (2h/day)

## Daily Structure
**Goal:** Learn one core concept + implement small task

---

### Day 1: Connection & Basic Queries
**Topics:**
- Installing PostgreSQL (or using free tier like [Neon.tech](https://neon.tech))
- `asyncpg` (or `psycopg`) basics

**Task:**
Write Python script that:
1. Connects to DB
2. Creates `users` table
3. Inserts 3 test users

---

### Day 2: CRUD Operations  
**Topics:**
- `INSERT/UPDATE/DELETE`
- Parameterized queries (avoid SQL injection)

**Task:**
Build CLI tool (using `argparse`) to:
- Add user
- Delete user by ID  
- List all users

---

### Day 3: Indexes & Optimization  
**Topics:**
- Index types (B-tree, Hash)
- `EXPLAIN ANALYZE`

**Task:**
1. Add 10k dummy users  
2. Compare query speed:  
   - Without index  
   - With index on `email` field

---

### Day 4: Joins & Relationships  
**Topics:**
- 1-to-many relationships  
- `INNER/LEFT JOIN`  

**Task:**
1. Create `posts` table linked to `users`  
2. Write query: "Get all posts with author names"

---

### Day 5: Transactions & Errors  
**Topics:**
- `BEGIN/COMMIT/ROLLBACK`  
- Handling deadlocks  

**Task:**
Simulate money transfer:
1. Deduct from User A  
2. Add to User B  
3. Rollback if either fails

---

### Day 6: SQLAlchemy ORM  
**Topics:**
- Declarative Base  
- Session lifecycle  

**Task:**
Rewrite Day 2 CLI tool using SQLAlchemy

---

### Day 7: Integration with Bookstore Project  
**Task:**
Connect your FastAPI from Week 2 to PostgreSQL

---