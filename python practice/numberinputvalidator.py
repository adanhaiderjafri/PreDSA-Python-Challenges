try:
    number = int(input("number :"))
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("Execution Completed")