import re

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein"
]

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common and easily guessable.")
        score = 0

    return score, feedback


def strength_label(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter your password: ")

    score, feedback = check_password_strength(user_password)
    label = strength_label(score)

    print("\nPassword Strength:", label)

    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print("- " + tip)
    else:
        print("✔ Your password is secure.")
