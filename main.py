class User():
    def __init__(self, num, name, roi):
      self.num = num
      self.name = name
      self.roi = roi

    def acc_sum(self):
        print(f"\nPersonal Information\nAccount No: {self.num}\nName: {self.name}\nRate Of Interest: {self.roi}% ")
        
class ChequingAccount(User):
    def __init__(self, num, name, roi):
        super().__init__(num, name, roi)
        self.balance = 0
        self.overdraft_limit = 500

    def summary(self):
        self.acc_sum()
        print(f'Account Balance: ${self.balance:.2f}')

    def deposit (self,dep_amount):
        self.dep_amount = dep_amount
        self.balance += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw (self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.balance:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance avaliable: ${self.balance:.2f}')

class SavingAccount(User):
    def __init__(self, num, name, roi):
        super().__init__(num, name, roi)
        self.balance = 0
        self.overdraft_limit = 1000

    def summary(self):
        self.acc_sum()
        print(f'Account Balance: ${self.balance:.2f}')

    def deposit (self,dep_amount):
        self.dep_amount = dep_amount
        self.balance += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw (self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.balance:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance avaliable: ${self.balance:.2f}')

print('Welcome to the SS Bank!')
num = int(input('Please enter your Account Number: '))
name = input('Please enter your name: ')
roi = int(input('Please enter rate of interest: '))
Chequing = ChequingAccount(num, name, roi)
Savings = SavingAccount(num, name, roi)

inAccountSelection = True

while inAccountSelection:
    acc_type = input(f"\nHello there {name}. Which account would you like to access today?\nType 'c' for checking account\nType 's' for savings account\nType 'q' to quit the system\n: ").lower()
    
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

    elif acc_type == 'q':
        inAccountSelection = False 
    
    else:
        print('That is an invalid command. Please try again!')

print('Thank you for using the SS Bank!')