#This is a simple calculator program

from math import *
print(""" 
This is a simple calculator prgram
These are the operations that you can enter:
    ______________________________
    |                            |
    | operation::symbol to enter |
    |____________________________|
      addition :: +
  substraction :: -
multiplication :: *
      division :: /
          sine :: sin
        cosine :: cos
       tangent :: tan
       exp sin :: sinh
       exp cos :: cosh
       exp tan :: tanh
   square root :: sqrt
      
""")
starter = True

while starter:
    message = input("What is the operation you would like to perform(enter quit to end): ")

    if message == "+":
        prompt = input("Do you know the number of digits to add or you want to keep adding until you are satisfied(Enter y for Yes or no for NO): ")
        if prompt.lower() == "y":

            number_of_items = input("How many items do you want to sum up: ")
            if number_of_items == "quit":
                break
            else:
                number_of_items = int(number_of_items)
                sum = 0
                for number in range(number_of_items):
                    singlenumber = float(input("Enter number: "))
                    sum += singlenumber
                    print(f"N = {number+1}")
                    print(f"Sum = {sum}.")
        elif prompt.lower() == "n":
            first_number = input("Enter number: ")
            if first_number.lower() == "quit":
                break
            second_number = input("Enter number: ")
            if second_number.lower() == "quit":
                break
            answer = float(first_number) + float(second_number)
            print(f"Sum = {answer}")
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")


        else:
            print("You must enter either y or n.")
        
    elif message == "*":
        prompt = input("Do you know the number of digits to multiply or you want to keep multiplying till you are satisfied(Enter y for YES or no for NO): ")
        if prompt.lower() == "y":
            number_of_items = input("How many items do you want to multiply or enter quit to exit: ")
            if number_of_items == "quit":
                break
            else:
                number_of_items = int(number_of_items)
                multiplication_total= 1
                for number in range(number_of_items):
                    singlenumber = float(input("Enter number: "))
                    multiplication_total*=singlenumber
                    print(f"N = {number}")
                    print(f"Multiplication total = {multiplication_total}")
        elif prompt.lower() == "n":
            first_number = input("Enter number: ")
            secondnumber = input("Enter number: ")
            if secondnumber.lower() != "quit":
                multiplication_total = float(first_number) * float(secondnumber)
                print(f"Multiplication total = {multiplication_total}")
                new_answer = multiplication_total
                while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

            if secondnumber.lower() == "quit":
                    break
        else:
            print("You must enter either y or no.")

    elif message == "-":
        while True:
            first_number = input("What is the number you want to subtract from: ")
            if first_number == "quit":
                break
            second_number = input("What is the number you want to subtract: ")
            if second_number == "quit":
                break
            answer = float(first_number) - float(second_number)
            print(answer)
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

       
    elif message == "/":
         while True:
            first_number = input("What is the number you want to divide: ")
            if first_number == "quit":
                break
            second_number = input("What is the number you want to divide with: ")
            if second_number == "quit":
                break
            answer = float(first_number)/float(second_number)
            print(answer)
            new_answer = answer

            while True:
                second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                second_step = second_step.lower()
                if second_step == "quit":
                    break
                if second_step == "+":
                    new_number = input("What is the number: ")
                    new_answer = float(new_answer)+float(new_number)
                elif second_step == "*":
                    new_number = input("What is the number: ")
                    new_answer = float(new_answer)*float(new_number)
                elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                elif second_step == "/":
                    new_number = input("What is the number: ") 
                    new_answer = float(new_answer)/float(new_number) 
                elif second_step == "sin":
                    new_answer = sin(new_answer)
                elif second_step == "cos":
                    new_answer = cos(new_answer)
                elif second_step == "tan":
                    new_answer = tan(new_answer)
                elif second_step == "sinh":
                    new_answer = sinh(new_answer)
                elif second_step == "cosh":
                    new_answer = cosh(new_answer)
                elif second_step == "tanh":
                    new_answer = tanh(new_answer)
                elif second_step == "sqrt":
                    new_answer = sqrt(new_answer)
                else: 
                    print("Invalid operation.")


     
    elif message == "sin":
        parameter = input("Input your number: ")
        parameter = int(parameter)
        answer = sin(parameter)
        try:
            print(answer)
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "tan": 
        parameter = input("Input your number: ")
        parameter = int(parameter)
        answer = tan(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "cos": 
        parameter = input("Input your number: ")
        parameter = int(parameter)
        answer = cos(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "sinh": 
        parameter = input("Input your number: ")
        parameter = float(parameter)
        answer = sinh(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "cosh": 
        parameter = input("Input your number: ")
        parameter = float(parameter)
        answer = cosh(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "tanh": 
        parameter = input("Input your number: ")
        parameter = float(parameter)
        answer = tan(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "tanh":
                        new_answer = tanh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "sqrt": 
        parameter = input("Input your number: ")
        parameter = float(parameter)
        answer = sqrt(parameter)
        try:
            print(answer)
            new_answer = answer
            while True:
                    second_step = input(f"What is the next operation on {new_answer}, input quit to go back: ")
                    second_step = second_step.lower()
                    if second_step == "quit":
                        break
                    if second_step == "+":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)+float(new_number)
                    elif second_step == "*":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)*float(new_number)
                    elif second_step == "-":
                        new_number = input("What is the number: ")
                        new_answer = float(new_answer)-float(new_number)
                    elif second_step == "/":
                        new_number = input("What is the number: ") 
                        new_answer = float(new_answer)/float(new_number) 
                    elif second_step == "sin":
                        new_answer = sin(new_answer)
                    elif second_step == "cos":
                        new_answer = cos(new_answer)
                    elif second_step == "tan":
                        new_answer = tan(new_answer)
                    elif second_step == "sinh":
                        new_answer = sinh(new_answer)
                    elif second_step == "cosh":
                        new_answer = cosh(new_answer)
                    elif second_step == "sqrt":
                        new_answer = sqrt(new_answer)
                    else: 
                        print("Invalid operation.")

        except:
            print("Error Error")


    elif message == "quit":
        break


    else:
        print("This is not a valid input. ")

    
