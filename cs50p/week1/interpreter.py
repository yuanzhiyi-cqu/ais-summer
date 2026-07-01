expression = input("Expression: ")

x, operator, y = expression.split()

x = float(x)
y = float(y)

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

print(result)