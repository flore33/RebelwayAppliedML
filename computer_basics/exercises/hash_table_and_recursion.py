def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(6))  # Output: 8

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120


def char_frequency(s):
    # Your code here string:"hello"
    freq = {}
    for char in s:
        print(f"char: '{char}'")
        #string.append(char)
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def first_non_repeating_character(s):
    length = len(s)
    for i in range(length):
        found = 0
        for j in range(length):
            if i != j and s[i] == s[j]:
                found =True
                break 
        if not found:
            return s[i]
    return None
    

def two_sum_digits(nums:list[int], target:int):
    index = 0
    for i in range(len(nums)):
        print(f" i: '{i}'")
        for j in range(i+1,len(nums)):
            print(f" i: '{i}'")
            if nums[i] + nums[j] == target:
                print(f" j: '{j}', i: '{i}'")
                return [i, j]
    return None
            
def sum_digits(n):
    string = str(n)
    total = 0
    if n == 0:
        return 0
    for i in range(len(string)):
        print(f" i: '{i}'")
        total += int(string[i])    

    return total

#recurssive version
def sum_digits_recurssion(n):
    print(f"Calling sum_digits({n})")  # Debug: show each call
    if n == 0:
        print("Base case reached: return 0")
        return 0
    else:
        last_digit = n % 10
        remaining = n // 10
        print(f"last_digit: {last_digit}, remaining: {remaining}")
        result = last_digit + sum_digits(remaining)
        print(f"Returning: {last_digit} + sum_digits({remaining}) = {result}")
        return result



def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
#def is_palindrome(s):
    return s == reverse_string(s)

def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
    


        
        

   
        
      



            
                

    

#print(char_frequency("hello"))
#print(first_non_repeating_character("swiss"))
#print(two_sum_digits([2, 7, 11, 13], 9))
#print(sum_digits(12345))
#print(reverse_string("recurssion"))
#print(is_palindrome("madam"))
#print(sum_digits_recurssion(1234))
#print(test("madame"))