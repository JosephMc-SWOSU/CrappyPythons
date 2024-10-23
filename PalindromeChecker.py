def getuserword():
    return input("Please enter a word to check if it is a Palindrome: ")

def ispalindrome(word):
    return word == word[::-1]

if __name__ == "__main__":

    userword = getuserword()
    if ispalindrome(userword):
        print("The word you entered is a Palindrome.")
    else:
        print("The word you entered is not a Palindrome.")