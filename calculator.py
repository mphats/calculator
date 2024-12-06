# Basic Calculator Program  

# Function to perform the selected operation  
def calculate(num1, num2, operation):  
    if operation == '+':  
        return num1 + num2  
    elif operation == '-':  
        return num1 - num2  
    elif operation == '*':  
        return num1 * num2  
    elif operation == '/':  
        if num2 != 0:  
            return num1 / num2  
        else:  
            return "Error: Division by zero"  
    else:  
        return "Error: Invalid operation"  

# Main program  
def main():  
    # User input  
    try:  
        number1 = float(input("Enter the first number: "))  
        number2 = float(input("Enter the second number: "))  
        operation = input("Enter the operation (+, -, *, /): ")  

        # Calculate and display the result  
        result = calculate(number1, number2, operation)  

        # Display the result  
        if isinstance(result, str):  # Check if there's an error message  
            print(result)  
        else:  
            print(f"{number1} {operation} {number2} = {result}")  
    except ValueError:  
        print("Error: Please enter valid numbers.")  

# Run the calculator program  
if __name__ == "__main__":  
    main()