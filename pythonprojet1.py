def analyze_password_strength(password):
    suggestions = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
   
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in "@#_":
            has_special = True
        
    if has_upper:
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    if has_lower:
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    if has_digit:
        score += 1
    else:
        suggestions.append("Include at least one digit.")

    if has_special:
        score += 1
    else:
        suggestions.append("Include at least one special character @#_.")

    if score == 5:
        return "Strong password!", []
    elif score == 4:
        return "Good password, but could be stronger.", suggestions
    else:
        return "Weak password!", suggestions
    

password = input("Enter your password: ")
strength, suggestions = analyze_password_strength(password)
print(f"Password Strength: {strength}")
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")