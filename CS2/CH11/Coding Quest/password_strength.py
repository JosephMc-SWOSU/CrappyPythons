import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    if all([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria]):
        return "Strong password"
    else:
        feedback = "Weak password. Improve by ensuring the following:\n"
        if not length_criteria:
            feedback += "- At least 8 characters long\n"
        if not digit_criteria:
            feedback += "- Contains at least one digit\n"
        if not uppercase_criteria:
            feedback += "- Contains at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Contains at least one lowercase letter\n"
        if not special_char_criteria:
            feedback += "- Contains at least one special character (e.g., !@#$%^&*)\n"
        return feedback

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)