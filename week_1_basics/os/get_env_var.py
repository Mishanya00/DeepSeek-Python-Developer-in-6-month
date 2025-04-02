import os


name = os.getenv("MY_NAME", "World")

print(f"Hello {name} from Python")
