def add(a,b):
    return a+ b
def multiply(a,b):
    return a * b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
print("calculator launched")
user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))
operation_choice = input("Enter operation sign(+,-,*,/): ")
if operation_choice == "+":
    print(f"the sum is {add(user_input1,user_input2)}")
elif operation_choice == "-":
    print(f"subtraction result is : {subtract(user_input1,user_input2)}")
elif operation_choice == "*":
    print(f"multiplication is {multiply(user_input1,user_input2)}")
elif operation_choice == "/":
    print(f"division is {divide(user_input1,user_input2)}")
else:
    print("you have not entered an operation sign")