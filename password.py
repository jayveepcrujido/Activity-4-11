import re


def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'\d', password)
    special = re.search(r'[\W_]', password)

    if all([length, upper, lower, digit, special]):
        return "Strong"
    elif length and (upper or lower) and digit:
        return "Medium"
    else:
        return "Weak"
