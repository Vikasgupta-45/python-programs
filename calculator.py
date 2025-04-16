# Aim: Write a Program to make simple calculator using if statements
# Branch: com
# Year: 2
# Sem: four
# Subject:python
# Name: Shaikh Mohd Ashfaque
# UIN:231po50
# Roll No.:37

print("***************************")
print("Simple Calculator")
print("shaikh maviya ")
print("***************************")


while True:
    # Displaying the menu
    print("\nMENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.power")
    print(". Exit")

    # Taking user input for the operation choice
    choice = int(input("Enter your choice: "))

    if choice >= 1 and choice <= 5:
        # Prompting for two numbers
        print("Enter two numbers: ")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        # Performing the selected operation
        if choice == 1:
            res = num1 + num2
            print("Result = ", res)
        elif choice == 2:
            res = num1 - num2
            print("Result = ", res)
        elif choice == 3:
            res = num1 * num2
            print("Result = ", res)
        elif choice == 4:
            if num2 != 0:
                res = num1 / num2
                print("Result = ", res)
            else:
                print("Error! Division by zero.")
        elif choice==5:
            res=num1**num2
            print("Result = ", res)


    elif choice == 6:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Wrong input..!! Please enter a valid choice.")