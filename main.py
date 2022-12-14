class Account():
    def __init__(self, num, name, roi, balance): #created constructor
      self.num = num #define parameters
      self.name = name
      self.roi = roi
      self.bal = balance

    def acc_sum(self): #displays the summary of account no, name and rate of interest
        print(f"\nPersonal Information\nAccount No: {self.num}\nName: {self.name}\nRate Of Interest: {self.roi}% ")

    def getName(self): #returns the name
        return self.name   

class ChequingAccount(Account):
    def __init__(self, num, name, roi, balance):
        super().__init__(num, name, roi, balance)
        self.overdraft_limit = 500

    def summary(self): #displays the summary of balance in the account
        self.acc_sum()
        print(f'Account Balance: ${self.bal:.2f}')

    def deposit (self,dep_amount):  # Function for depositing money
        self.dep_amount = dep_amount
        self.bal += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.bal:.2f} with overdraft limit of: ${self.overdraft_limit:.2f}')
        print(f'Your total account balance is: ${self.bal + self.overdraft_limit:.2f}')

    def withdraw (self,withdraw_amount): # Function for withdrawing money
        self.withdraw_amount = withdraw_amount
        if self.bal >= withdraw_amount - self.overdraft_limit:
            self.bal -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.bal:.2f} with overdraft limit of: ${self.overdraft_limit:.2f}')
            print(f'Your total account balance is: ${self.bal + self.overdraft_limit:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance available: ${self.bal:.2f} with overdraft limit of: ${self.overdraft_limit:.2f}')
            print(f'Your total account balance is: ${self.bal + self.overdraft_limit:.2f}')

class SavingAccount(Account):
    def __init__(self, num, name, roi, balance):
        super().__init__(num, name, roi, balance)
        self.min_limit = 1000

    def summary(self): #displays the summary of balance in the account
        self.acc_sum()
        print(f'Account Balance: ${self.bal:.2f}')

    def deposit (self,dep_amount):  # Function for depositing money
        self.dep_amount = dep_amount
        self.bal += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.bal:.2f} with overdraft limit of: ${self.min_limit:.2f}')
        print(f'Your total account balance is: ${self.bal + self.min_limit:.2f}')

    def withdraw (self,withdraw_amount): # Function for withdrawing money
        self.withdraw_amount = withdraw_amount
        if self.bal >= withdraw_amount - self.min_limit:
            self.bal -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.bal:.2f} with overdraft limit of: ${self.min_limit:.2f}')
            print(f'Your total account balance is: ${self.bal + self.min_limit:.2f}') 
        else:
            print(f'You have insufficent funds. Please try again.\nBalance available: ${self.bal:.2f} with minimum limit of: ${self.min_limit:.2f}')
            print(f'Your total account balance is: ${self.bal + self.min_limit:.2f}')

#Admin new customer profile and exisitng profile access
print('Welcome to SS Bank!')
num = int(input('Please enter your Account Number: ')) #asks for account number
name = input('Please enter your name: ') #asks for name
roi = int(input('Please enter rate of interest: ')) #asks for rate of interest
balance = int(input("Enter your balance: $")) #asks for the amount in the balance

Chequing = ChequingAccount(num, name, roi, balance)
Savings = SavingAccount(num, name, roi, balance)

asif=Account(1234,"asif", 4, 1200) #creates an array
audrey=Account(1235,"audrey", 4, 1200)
george=Account(1236,"george", 4, 1200)
harneet=Account(1237,"harneet", 2, 1200)
areeba=Account(1238, "areeba", 2, 1200)

list=[asif, audrey, george, harneet, areeba]

for acc in list:
    if (acc.getName()).lower==(name).lower:
       acc.acc_sum() 

inAccountSelection = True

while inAccountSelection: #Admin menu after login function
    acc_type = input(f"\nHello there {name}. Which account would you like to access today?\nType 'c' for chequing account\nType 's' for savings account\nType 'q' to quit the system\n: ").lower()
    
    if acc_type == 'c':
        session = True
        while session:
            act = input("\nType 'd' to deposit money\nType 'w' to withdraw money\nType 'sum' to view a summary of your account\nType 'm' to go to main menu\n: ").lower()
            if act == 'd':
                dep_amount = float(input('How much would you like to deposit?: '))
                Chequing.deposit(dep_amount)
            elif act == 'w':
                with_amount = float(input('How much would you like to withdraw? '))
                Chequing.withdraw(with_amount)
            elif act == 'sum':
                Chequing.summary()
            elif act == 'm':
                session = False
            else:
                print('Invalid input. Please try again.')

    elif acc_type == 's':
        session = True
        while session:
            act = input("\nType 'd' to deposit money\nType 'w' to withdraw money\nType 'sum' to view a summary of your account\nType 'm' to go to main menu\n: ").lower()
            if act == 'd':
                dep_amount = float(input('How much would you like to deposit?: '))
                Savings.deposit(dep_amount)
            elif act == 'w':
                with_amount = float(input('How much would you like to withdraw? '))
                Savings.withdraw(with_amount)
            elif act == 'sum':
                Savings.summary()
            elif act == 'm':
                session = False
            else:
                print('Invalid input. Please try again.')

    elif acc_type == 'q': #allows the user to quit
        inAccountSelection = False 
    
    else:
        print('That is an invalid command. Please try again!')

print('Thank you for visiting SS Bank. Have a nice day!')