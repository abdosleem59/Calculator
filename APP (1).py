def print_menu():
    print('''\nMenu:
Enter 1 to sum from 1 to N
Enter 2 to evaluate simple 2 numbers expression (e.g 2 + 3)
Enter 3 to end the program''')
        

def sum_1_to_n():
    numberN = int(input("\nEnter a number: "))
    resOfSequenceFrom1toN = (numberN+1) * (numberN/2)
    print("Sum from 1 to", numberN, "is", resOfSequenceFrom1toN, "\n")


def expression():
    operand1,operation,operand2 = map(str,input("\nEnter a simple expression: ").split())
    operand1 = float(operand1)
    operand2 = float(operand2)
    res = None
    
    if operation == '/' or operation == "//":
        divide(operand1, operand2, operation)

    else: 
        if operation == '+':
            res = operand1+operand2
        if operation == '-':
            res= operand1-operand2
        if operation == '*':
            res = operand1*operand2
        if operation == '**':
            res = operand1 ** operand2
        
        print("Expression value is:", res )
        print()



def divide(operand1, operand2, operation):
    if operand2 == 0:
        print("Sorry: No way to compute this expression")
    else:
        if operation == '/':
            res = operand1/operand2
        elif operation == '//':
            res = operand1//operand2

        print("Expression value is:", res )
        print()


def calculator_interface():
    while True:
        print_menu()
        choice = int(input("Enter choice from 1 to 3: "))
        if 1 < choice > 3:
            print("Invalid input...Try again!\n")
        elif choice==1:
            sum_1_to_n()

        elif choice == 2:
            expression()

        elif choice == 3:
            print("\nThank you.")
            break
        

calculator_interface()
