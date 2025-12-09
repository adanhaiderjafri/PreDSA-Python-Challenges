try:
    number1 = int(input("number1 :"))
    number2 = int(input("number2 :"))
    Result  = number1 / number2
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Please in denominator put a value greater than Zero!")
else:
    print(f"The result is {Result}")
finally:
    print("Program Executed!")