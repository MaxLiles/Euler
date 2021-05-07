def isPalindrome(x): 
    string = str(x)

    max_length = len(string)
    halfway = int(max_length /2)
    first = string[0: halfway]
    second = string[halfway: max_length]
    
    return True if first == second[::-1] else False

