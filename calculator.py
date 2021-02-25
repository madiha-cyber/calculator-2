"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Replace this with your code

while True:

    user_input = input("what equation do you want to solve: ")
    tokens = user_input.split(' ')
    operator = tokens[0]
    if user_input == "q":
        print("Goodbye")
        break
    elif len(tokens) < 2:
        print("not enough inputs")
        continue
    elif len(tokens) > 3:
        print("Too many inputs")
        continue
    elif len(tokens) == 2:
        if operator != "square" and operator !="cube":
            print("Error!, Not enough inputs")
            continue

    # if user provides too many inputs
    # if len(tokens) > 3:
    #     num3 = tokens[3]
    # elif len(tokens) < 3:
    #     num2 = '0'
    # else:
    #     num2 = tokens[2]

    # if len(tokens) < 3:
    #     num2 = "0"
    # else:
    #     num2 = tokens[2]

    # if len(tokens) > 3:
    #     num3 = tokens[3]

    if operator == "+":
        result = add(float(tokens[1]), float(tokens[2]))
    elif operator == "-":
        result = subtract(float(tokens[1]), float(tokens[2]))
    elif operator == "*":
        result = multiply(float(tokens[1]), float(tokens[2]))
    elif operator == "/":
        result = divide(float(tokens[1]), float(tokens[2]))
    elif operator == "square":
        result = square(float(tokens[1]))
    elif operator == "cube":
        result = cube(float(tokens[1]))
    elif operator == "pow":
        result = power(float(tokens[1]), float(tokens[2]))
    elif operator == "mod":
        result = mod(float(tokens[1]), float(tokens[2]))

    print(result)