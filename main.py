# This is a sample Python script.
import random


class Account:
    fname =''
    lname=''
    add=''
    tel=''

    def __init__(self):
        self.fname=input('Enter first name: ')
        self.lname=input('Enter last name: ')
        self.add=input('Enter address: ')
        self.tel=input('Enter phone number: ')

    def display(self):
        range_start = 10**(10-1)
        range_end = (10**10)-1
        accountnum =random.randint(range_start,range_end)
        print('Account#: '+str(accountnum)+'\n '+self.fname
              + ' '+self.lname+' ' + self.add+' '+self.tel)

class BankAccount(Account):
    def __init__(self):
        self.balance = 0
        print("Hello!!! Would you like to a Deposit and or Withdrawal Today")
        super().display()

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")


    def display(self):
            print("\n Net Available Balance=", self.balance)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make =input('Welcome to Milord Bank enter yes to make an account or enter no! ')
    if make =='Yes':
        account1 = Account()
        account1.display()
        bal = BankAccount()
    else:
        print('Have a Nice Day!')
        exit()

    counter = 1
while (counter <= 5):
    print('Maximun is 5 a day deposit and withdraw')
    chose = int(input("Enter 1 for Deposit or 2 for Withdrawal: "))
    if chose == 1:
        bal.deposit()
    elif chose == 2:
        bal.withdraw()
    counter += 1
    bal.display()
