from divide import divide

try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
except ValueError as e:
    print(f"Error: invalid input! {e}")
else:
    print("Result:", divide(num1, num2))
