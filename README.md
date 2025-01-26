def palidromy(word):
    """
        Checks if a given word is a palindrome and prints the result.

        Arguments:
        word: A string representing the word to be checked.

        The function reverses the input word and compares it to the original.
        If both are the same, it prints that the word is a palindrome; otherwise, 
        it prints that the word is not a palindrome.
    """
    paliword = ""
    for letter in word[::-1]:  # Using slicing to reverse the word
        paliword += letter  

    if paliword == word:
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is NOT a palindrome')
