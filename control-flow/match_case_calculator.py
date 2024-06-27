def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose the operation (+, -, *, /): ")

    result = match_case(operation, num1, num2)
    print("The result is:", result)


def match_case(operation, num1, num2):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Error: Invalid operation"


calculator()
