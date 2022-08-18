#!/usr/bin/env python3
#python project

def financial_calculator():
    """ Calculate your Car or Mortgage payment"""
    try:
        price = float(input(" What is the total price of your car or home? Please enter the numeric value:\n>"))
        downpayment = float(input( "How much money you would like to put as downpayment? Please enter the numeric value:\n>"))
        loan_amount = price - downpayment

        loanterm = int(input("What is the length of the loan in years? Please enter the numeric value:\n>"))
        #Claculate the loan length in months
        loanterm_month = loanterm * 12
        
        #print(monthly_payment)
        interestrate = float(input("What is the yearly interest rest?\n>"))
        monthly_rate = interestrate / 12 /100
        #    print(monthly_rate)     
        #Calculate the monthly payment
        monthly_payment = (monthly_rate * loan_amount * pow((1 + monthly_rate), loanterm_month))  / (pow((1 + monthly_rate), loanterm_month) - 1)
        monthly_payment = "{:.2f}".format(monthly_payment)
    #    print(f'Your monthly payment is: {monthly_payment}') 
        return  f'Your monthly payment is: {monthly_payment}'
    #except OverflowError:
        #return "The error occurred because xyz"
    except ValueError:
        return "That was not a number. Please put a number."
    except:
        return "There was an error!"

def another_payment():
    wrong_input = 0    
    while True:
        another_pay = input("Do you have another payment to calculate? Answer Y/N")
        another_pay = another_pay.strip().lower()
        if another_pay == "y":
            print(financial_calculator()) 
        elif another_pay == 'n':
            print ("Thank you. Have a nice day.")
            break
        else:
            wrong_input += 1
            if wrong_input > 3:
                print("Wrong input entered too many times. Please contact customer service")
                break
            print("That wasn't one of the options!")

def main():
    print(financial_calculator())
    #print("Your monthly payment is...")
    #print("There was an error!")
    another_payment()

if __name__ == "__main__":
    main()
