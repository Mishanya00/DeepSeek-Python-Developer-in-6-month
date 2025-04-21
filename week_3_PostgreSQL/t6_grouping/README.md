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