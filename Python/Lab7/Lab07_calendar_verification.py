print("="*40)
print("     CALENDAR VERIFICATION SYSTEM       ")
print("="*40)
year=int(input("Enter year: "))
if year<=0:
    print("Error: You need to enter a positive integer")
if year % 100 == 0:
    if year % 400 == 0:
        status="Leap Year"
        total_days=366
        days_in_feb=29
        reason="Century year divisible by 400"
    else:
        status="Common Year"
        total_days=365
        days_in_feb=28
        reason="Century year not divisible by 400"
else:
    if year % 4 == 0:
        status="Leap Year"
        total_days=366
        days_in_feb=29
        reason="Divisible by 4 and not a century year"
    else:
        status="Common Year"
        total_days=365
        days_in_feb=28
        reason="Not divisible by 4"
print("-"*40)
print(f"Year: {year}")   
print(f"Status: {status}")
print(f"Days in Year: {total_days} days")
print(f"Days in February: {days_in_feb} days")
print(f"Reason: {reason}")
