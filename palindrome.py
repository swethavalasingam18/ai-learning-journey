word =input("enter the word: ")
def is_palindrome(text):
    # s[::-1] creates a reversed copy of the string
    return text == text[::-1]

# Example usage:
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
