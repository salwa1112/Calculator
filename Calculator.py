# Python program for simple calculator
while True:
    print("This is a calculator. Please select one of the following operations -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n")
    try:
        select = str(input("Enter choice(1/2/3/4): "))
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2nd number: "))
        if select == "1":
            print(number_1, "+", number_2, "=", number_1+number_2)
        elif select == "2":
            print(number_1, "-", number_2, "=", number_1-number_2)

        elif select == "3":
            print(number_1, "*", number_2, "=", number_1*number_2)

        elif select == "4":
            print(number_1, "/", number_2, "=", number_1/number_2)
        else:
            print("Selection choice is invalid.")
            continue
    except ZeroDivisionError:
        print("Number can not be divisible by zero")
    except (ValueError, TypeError):
        print('Invalid Input!')
    finally:
        print('GOODBYE')

        key_press = str(input(
            "Please write \"quit\" and press ENTER to stop the calculator else press any key and ENTER to continue: "))
        if(key_press == "quit"):
            break
