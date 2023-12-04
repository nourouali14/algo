def is_palindrome(word):
    # Base case: an empty word or a word with a single character is a palindrome
    if len(word) <= 1:
        return True
    
    # Compare the characters at the ends of the word
    if word[0] == word[-1]:
        # Recursively check the rest of the word
        return is_palindrome(word[1:-1])
    else:
        # If the characters at the ends are different, it's not a palindrome
        return False


