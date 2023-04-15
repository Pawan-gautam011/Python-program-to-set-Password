password=input("Enter a password:")
if len(password)<8:
    print("Password must contain at least 8 character long")

else:
    has_upper=False
    has_lower=False
    has_digit=False
    for char in password:
        if char .isupper():
            has_upper=True
        elif char .islower():
            has_lowercase=True
        elif char .isdigit():
            has_digit=True
    if not(has_upper and has_lower and has_digit):
        print("Password must contain at least one uppercase letter,one lowercase letter and one digit.")
    else:
        print(password,"is valid")