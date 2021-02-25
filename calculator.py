"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


while True:
    user_input = input("what equation do you want to solve")
    token = user_input.split(' ')
    operator = token[0]
   
    if user_input == "q":
        print("Goodbye")
        break
    elif operator == "+":
        add(int(token[1]), int(token[2]))
    elif operator == "-":
        subtract(int(token[1]), int(token[2]))
    elif operator == "*":
        multiply(int(token[1]), int(token[2]))
    elif operator == "/":
        divide(int(token[1]), int(token[2])) 
    elif operator == "square":
        square(int(token[1])) 
    elif operator == "cube":
        cube(int(token[1]))  
    elif operator == "pow":
        power(int(token[1]), int(token[2]))  
    elif operator == "mod":
        mod(int(token[1]), int(token[2]))              