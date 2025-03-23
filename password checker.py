import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password!", feedback

password = input("Enter a password to check its strength: ")
strength_message, suggestions = assess_password_strength(password)
print(strength_message)
for tip in suggestions:
    print("-", tip)
