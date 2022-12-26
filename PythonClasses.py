from pathlib import Path

path = Path("C:\python project\ecommerce")
for i in path.glob("*.py"):
    print(i)


