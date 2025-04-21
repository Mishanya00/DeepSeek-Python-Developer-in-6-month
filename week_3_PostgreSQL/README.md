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
   - With index on `name` field

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

### Day 6: SQL Grouping Operations

**Topics:**

1. **GROUP BY fundamentals**
   - Aggregation functions (COUNT, SUM, AVG)
   - Filtering groups with HAVING
2. **Advanced grouping**
   - ROLLUP/CUBE for subtotals
   - GROUPING SETS
3. **Window functions**
   - PARTITION BY
   - ROW_NUMBER(), RANK(), DENSE_RANK()
   - Running totals (SUM() OVER)

## Tasks:

### Task 1: Basic Grouping

Using your bookstore database:

```sql
-- 1. Count books per author
-- 2. Find average book price by genre
-- 3. List genres with >3 books (HAVING)

---

### Day 7: Integration with Bookstore Project

**Task:**
Connect your FastAPI from Week 2 to PostgreSQL

---