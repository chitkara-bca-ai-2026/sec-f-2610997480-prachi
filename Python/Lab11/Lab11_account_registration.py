print("Input:")
username=input("Enter your Username: ")
password=input("Enter your Password: ")
min_length=len(password)>=8
has_digit=any(char.isdigit() for char in password)
has_upper=any(char.isupper() for char in password)
length_status="Pass" if min_length else "Fail"
digit_status="Pass" if has_digit else "Fail"
upper_status="Pass" if has_upper else "Fail"
is_valid=min_length and has_digit and has_upper
print()
print("Enter your username: Enter your password: ")
print("="*40)
print("PASSWORD VALIDATION RESULTS")
print("="*40)
print(f"Username: {username}")
print(f"Password: {'*'*len(password)}")
print()
print("---Validation rules---")
print(f"[{length_status}] Minimum 8 characters ({len(password)} characters)")
print(f"[{digit_status}] At least one digit")
print(f"[{upper_status}] At least one uppercase letter")
print("---Result---")
if is_valid:
    print("Password is valid.")
    print(f"Account created successfully for user {username}!.")
else:
    print("Password is invalid.")
print()
print("="*40)