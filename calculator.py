
while True:
    num1 = float(input("Number 1:"))
    oper = input("Operator:")
    num2 = float(input("Operator:"))

    if oper == "+":
        result = num1 + num2
    elif oper == "-":
        result = num1 - num2
    elif oper == "*":
        result = num1 * num2
    elif oper == "/":
        result = num1 / num2
    else:
        print("Enter a valid operator")
        continue

    user_input = input("Do you want to perform another operation? (yes/no): ").lower()
    if user_input != 'yes':
        break 

    #I'm not very impressed by this I want to be able to do multiple calculations at once
    #I'll come back to it.It's something to do with tuples or something