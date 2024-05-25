while True:
    print('''\nMenu:
Enter 1 to sum from 1 to N
Enter 2 to evaluate simple 2 numbers expression (e.g 2 + 3)
Enter 3 to end the program''')
    
    choice = int(input("Enter choice from 1 to 3: "))
    if 1 < choice > 3:
        print("Invalid input...Try again!\n")
        continue
    else:
        if choice == 1:
            numberN = int(input("Enter a number: "))
            resOfSequenceFrom1toN = (numberN+1) * (numberN/2)
            print("Sum from 1 to", numberN, "is", resOfSequenceFrom1toN, "\n")
        elif choice == 2:
            operand1,operation,operand2 = map(str,input("Enter a simple expression: ").split())
            operand1 = float(operand1)
            operand2 = float(operand2)
            res = None
            if operation == '/' or operation == "//" and operand2 == 0:
                print("Sorry: No way to compute this expression")
            else:
                if operation == '+':
                    res = operand1+operand2
                if operation == '-':
                    res= operand1-operand2
                if operation == '*':
                    res = operand1*operand2
                if operation == '/':
                    res = operand1/operand2
                if operation == '//':
                    res = operand1//operand2
                if operation == '**':
                    res = operand1 ** operand2
            
                print("Expression value is", res )
            print("\n")
        elif choice==3:
            break
            

            






