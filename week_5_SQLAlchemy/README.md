# Week 5: SQLAlchemy Essentials (2h/day)

## Daily Structure

**Goal:** Master SQLAlchemy ORM + advanced patterns

---

### Day 1: SQLAlchemy Setup

**Topics:**

- ORM vs Core
- Declarative Base
- Session lifecycle

**Task:**

1. Setup SQLAlchemy with PostgreSQL
2. Create `User` model with:
   - id (Integer PK)
   - name (String)
   - email (String, unique)

---

### Day 2: Relationships

**Topics:**

- 1-to-many
- many-to-many
- backref/back_populates

**Task:**

1. Add `Post` model linked to User
2. Implement:
   - Get user with posts
   - Create post for user

---

### Day 3: N+1 Problem

**Topics:**

- Eager loading
- Lazy loading
- Selectinload/Joinedload

**Task:**

1. Create N+1 scenario
2. Fix using:
   
   ```python
   session.query(User).options(selectinload(User.posts))
   ```

---

### Day 4: Advanced Queries

**Topics:**

- Hybrid properties
- Window functions
- Bulk operations

**Task:**

1. Add "post_count" hybrid property
2. Implement top 5 users by post count

---

### Day 5: Transactions

**Topics:**

- Session states
- Isolation levels
- Optimistic locking

**Task:**

1. Implement money transfer:
   - Deduct from A
   - Add to B
   - Rollback on error