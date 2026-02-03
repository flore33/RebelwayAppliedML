#stack = []

# Push
#stack.append(10)
##stack.append(20)

# Pop
#top = stack.pop()  # Removes 20

# Peek
#if stack:
#    print(stack[-1])  # Shows 10

# Check empty
#print(len(stack) == 0)  # False

#print(top)


#string = ["hello"]
#print(string)
#reversed_string = string[::-1]
#print(reversed_string)

import math

def reverse_string(string):
    result = ""
    for char in string:
        print(char)
        result = char + result
    return result

#print (reverse_string("heelo"))

def reverse_string_stack(string):
    stack = []
    for char in string:
        stack.append(char)

    reverse_string = ""
    while stack:
        reverse_string += stack.pop()

    return reverse_string
#print(reverse_string_stack("world"))

#function that checks if the parentheses in a string are balanced.
def parantheses_balance(data):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for c in data:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack or stack[-1] != pairs[c]:
                print(False,"unmatched parentheses")

                return False
            stack.pop()
    if not stack :
        print(True, "match parentheses")
    else:
        print(False, "unmatched parentheses")
        return False
        
    return(stack)

#data = "({}))"
#print(parantheses_balance("({[]})"))

    pass

    pass
def evaluate_postfix(arr:list[str]):
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for c in arr:
        # handle negative numbers
        if c.lstrip("-").isdigit():
            stack.append(int(c))

        elif c in operators: 
            if len(stack) < 2 :
                raise ValueError(f"Insufficient operand in '{c}'")
            
            right = stack.pop()
            left =stack.pop()

            if c == "+":
                stack.append(left + right)

            if c == "-":
                stack.append(left - right)

            if c == "*":
                stack.append(left * right)
            
            if c == "/":
                if right == 0:
                    raise ValueError(f"Division by zero")

                stack.append(math.trunc(left / right)) 
        
        else:
            raise ValueError("Invalid token '{c}'")

    if len(stack) != 1:
        raise ValueError("Postfix expression malformed")

    return(stack[0])

def evaluate_postfix_2(arr:list[str]):
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for c in arr:
        # handle negative float
        try:
            if "." in c:
                stack.append(float(c))
            else:
                stack.append(int(c))

        except ValueError:
            ("Invalid token '{c}'")

        if c in operators: 
            if len(stack) < 2 :
                raise ValueError(f"Insufficient operand in '{c}'")
            
            right = stack.pop()
            left =stack.pop()

            if c == "+":
                stack.append(left + right)

            if c == "-":
                stack.append(left - right)

            if c == "*":
                stack.append(left * right)
            
            if c == "/":
                if right == 0:
                    raise ValueError(f"Division by zero")

                stack.append(left / right)


    if len(stack) != 1:
       raise ValueError("Postfix expression malformed")

    return(stack[0])


arr = ["2", "3", "1", "*", "+", "9", "-"]
#arr = ["3.5", "2.0", "+", "4.5", "*"]
print(evaluate_postfix_2(arr))

#check size need to be pair otherwise missing
#if check pair divide in 2 and check for the first part == second 
