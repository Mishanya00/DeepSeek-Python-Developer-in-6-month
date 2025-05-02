### Day 1: Dependency Mastery

**Goal:** Build reusable service layer  
🔗 [FastAPI Dependencies Guide](https://fastapi.tiangolo.com/tutorial/dependencies/)  
✅ **Task:**  

1. Convert 2 routes to use class-based services  
2. Implement cached config loader:  
   
   ```python
   @lru_cache
   def get_settings():
    return Settings()
   ```