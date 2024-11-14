import re

def getuserword():
    return input("Please enter a word or phrase to check if it is a Palindrome: ")

def clean_word(word):
    # Remove non-alphanumeric characters and convert to lowercase
    return re.sub(r'[^A-Za-z0-9]', '', word).lower()

def ispalindrome(word):
    cleaned_word = clean_word(word)
    return cleaned_word == cleaned_word[::-1]

def main():
    while True:
        userword = getuserword()
        if ispalindrome(userword):
            print(f"The word or phrase '{userword}' is a Palindrome.")
        else:
            print(f"The word or phrase '{userword}' is not a Palindrome.")
        
        # Ask if the user wants to check another word
        again = input("Do you want to check another word or phrase? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
