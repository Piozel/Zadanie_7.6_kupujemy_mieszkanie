def is_palindrome(word):
    """ 
    Checks if a given word is a palindrome and returns the result.
    
    Arguments:
    word: A string representing the word to be checked.
    
    The function reverses the input word using slicing and compares it to the original.
    If both are the same, it returns True; otherwise, it returns False.
    """ 
 word == word[::-1]
