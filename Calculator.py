def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."
    else:
        return "Unsupported operation"

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation to perform (+, -, *, /): ")

        result = calculate(a, b, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()



