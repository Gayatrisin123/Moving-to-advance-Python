a = int(input("Enter a number: "))

try:
    result = 10 / a
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


print("Program continues after exception handling.")