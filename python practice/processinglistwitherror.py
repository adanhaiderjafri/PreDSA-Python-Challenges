values = [10, 0, "a", 5]

for item in values:
    try:
        num = 100 / item
        print(num)
    except (ValueError, ZeroDivisionError, TypeError):
        print("Invalid Value")
