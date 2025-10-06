# Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Simple Calculator")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Sum:", add(x, y))
print("Difference:", subtract(x, y))
print("Product:", multiply(x, y))
print("Quotient:", divide(x, y))
