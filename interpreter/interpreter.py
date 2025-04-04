expression = input("Expression: ")

x, y, z = expression.split()
value1 = float(x)
value2 = float(z)

if y == "+":
    print(value1 + value2)
elif y == "-":
    print(value1 - value2)
elif y == "x" or y == "*":
    print(value1 * value2)
elif y == "/":
    print(value1 / value2)
