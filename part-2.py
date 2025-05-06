# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    
    if array[0] == query:
        return True
        
    return search(array[1:], query)



# is_palindrome
def is_palindrome(s_input):
    if len(s_input) <= 1:
        return True
    
    if s_input[0] != s_input[-1]:
        return False
        
    return is_palindrome(s_input[1:-1])



# digit_match
def digit_match(number1, number2): 
    if number1 == 0 and number2 == 0:
        return 1

    elif number1 < 10 or number2 < 10:
        count_pairs = 0
        if number1 % 10 == number2 % 10:
            count_pairs += 1
        return count_pairs
    

    count_pairs = 0
    if number1 % 10 == number2 % 10:
        count_pairs += 1

    return count_pairs + digit_match(number1 // 10, number2 // 10)

