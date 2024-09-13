def is_palindrome(word):
    parsed_word = ''.join(char for char in word if char.isalnum())
    if parsed_word == parsed_word[::-1]:
        return f'\n{word} is a palindrome\n'
    else:
        return f'\n{word} is not a palindrome\n'

if __name__ == "__main__":
    test_word = input("\nEnter your word: ")
    print(is_palindrome(test_word))