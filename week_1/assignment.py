def calculator(): 
    while True:
        print("---Simple Calculator--")
        print("Input your numbers below and your mathematical operation when asked")
        try:
            num1 = int(input("Input your first number: "))
            num2 = int(input("Input your second number: "))
            operation = input("Input your operation from the list (*, -, +, /, //, **, %): ")
        
            match operation:
                case "*":
                    result = num1 * num2
                case "-":
                    result = num1 - num2
                case "+":
                    result = num1 + num2
                case "/":
                    if num2 == 0:
                        print("You can't divide a number by zero")
                        continue
                    result = num1 / num2
                case "//":
                    if num2 == 0:
                        print("You can't divide a number by zero")
                        continue
                    result = num1 // num2
                case "**":
                    result = num1 ** num2
                case "%":
                    result = num1 % num2
                case _:
                    print("Please input a valid operation")
                    continue
            print(f"{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Invalid input please enter numbers only")

        again = input("Do you want to perform another calculation? (yes/no)").strip().lower()

        if again != "yes":
            return False

calculator()

