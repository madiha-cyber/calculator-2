"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


while True:

    user_input = input("what equation do you want to solve")
    token = user_input.split(' ')
    operator = token[0]
    # num1 = token[1]
    
   
    if user_input == "q":
        print("Goodbye")
        break 

    elif len(token) < 2:
        print("not enough inputs")
        continue
    # if user provides too many inputs
    
    if len(token) > 3:
        num3 = token[3]
    
    elif len(token) < 3:
        num2 = '0'
    
    else:
        num2 = token[2]
    

    
    

    if len(token) < 3:
        num2 = "0"

    else:
        num2 = token[2]

    if len(token) > 3:
        num3 = token[3]

        
    


    if operator == "+":
        result = add(int(token[1]), int(token[2]))
    elif operator == "-":
        result = subtract(int(token[1]), int(token[2]))
    elif operator == "*":
        result = multiply(int(token[1]), int(token[2]))
    elif operator == "/":
        result = divide(int(token[1]), int(token[2])) 
    elif operator == "square":
        result = square(int(token[1])) 
    elif operator == "cube":
        result = cube(int(token[1]))  
    elif operator == "pow":
        result = power(int(token[1]), int(token[2]))  
    elif operator == "mod":
        result = mod(int(token[1]), int(token[2])) 
    
    print(result)             