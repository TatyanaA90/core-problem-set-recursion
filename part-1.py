# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    
    return n * factorial(n-1)



# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    
    return reverse(text[1:]) + text[0]



# bunny
def bunny(count):
    if count == 0:
        return 0
        
    return 2 + bunny(count-1)



# is_nested_parensdef is_nested_parens(parens):
def is_nested_parens(parens):
    return is_nested_helper(parens, 0)



def is_nested_helper(parens, count):
    if not parens:
        return count == 0  

    if parens[0] == '(':
        return is_nested_helper(parens[1:], count + 1)
    elif parens[0] == ')':
        if count == 0:
            return False  
        return is_nested_helper(parens[1:], count - 1)
    return False 
