#!/usr/bin/env python3
#python project

def financial_calculator():
    """ Calculate your Car or Mortgage payment"""
    price = ask_question("What is the total price of your car or home? ") 
    downpayment = ask_question("How much money will you put as downpayment? ")
    loan_amount = price - downpayment
    loanterm = int(ask_question("What is the length of the loan in years? "))
    #Claculate the loan length in months
    loanterm_month = loanterm * 12
    
    #print(monthly_payment)
    interestrate = float(input("What is the yearly interest rate?\n>"))
    monthly_rate = interestrate / 12 / 100
    #    print(monthly_rate)     
    #Calculate the monthly payment
    monthly_payment = (monthly_rate * loan_amount * pow((1 + monthly_rate), loanterm_month))  / (pow((1 + monthly_rate), loanterm_month) - 1)
    monthly_payment = "{:.2f}".format(monthly_payment)
    print(f'Your monthly payment is: {monthly_payment}') 

def ask_question(prompt):
    flag = True
    user_input = ""
    while flag:
        try:
            user_input = float((input(prompt)).strip().lower())
            flag = False
        except:
            print("Invalid input entered. Please try again")
    return user_input            

def main():
    flag = True 
    while flag:
        try:
            financial_calculator()
        except:
            if ValueError:
                print("tried reading invalid value: ", ValueError)
            elif ZeroDivisionError:
                print("error: tried dividing by zero: ")
            else:
                print("Sorry, you input an incorrect value")
        finally:
            user_input = ""
            wrong_count = 0
            while  (user_input != "y") and (flag != False):
                user_input = input("Would you like to calculate another payment? (y/n) ")
                user_input = user_input.strip().lower()
                if user_input == "n":
                    flag = False
                elif user_input != "y":
                    if wrong_count > 1:
                        flag = False
                        print("Wrong input entered too many times. Program quitting.")
                    else:
                        wrong_count += 1
                        print("Wrong input entered. Please try again.")


if __name__ == "__main__":
    main()
