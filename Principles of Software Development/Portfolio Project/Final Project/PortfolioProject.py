class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.attempts = 0
        self.max_attempts = 5
        self.access_granted = False

    def is_authenticated(self, pin):
        if pin == self.pin:
            self.access_granted = True
            print('Identity Verified.')
            return True
        else:
            self.attempts += 1
            print('\nIncorrect PIN.')
            print(f'Attempts: {self.attempts} \nAttempts remaining: {self.max_attempts - self.attempts}')
            return False

    def withdraw(self):
        withdraw_amount = prompt_for_number('\nEnter the amount you want to withdraw: $')
        self.check_funds(withdraw_amount)

    def check_funds(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f'New account balance: ${self.balance}\n')
            if self.balance == 0:
                print(f'Your balance is ${self.balance}. Your account will now be closed.')
                self.reset()
        elif withdraw_amount > self.balance:
            print('Insufficient funds.\n')
        return self.balance

    def reset(self):
        print('You have been logged out.')
        self.attempts = 0
        self.access_granted = False

def prompt_for_number(string):
    while True:
        try:
            user_input = float(input(string))
            if user_input is not ValueError:
                return user_input
        except ValueError:
            print('Enter a valid number.')

def main():
    # Create account
    print('----- Create Account -----')
    pin = input('Create your PIN: ')
    account_balance = prompt_for_number('Enter your account balance: $')

    account = ATM(pin, account_balance)

    # Authenticate user
    print('\n----- ATM Login -----')
    while True:
        try_pin = input('Enter your pin: ')
        if account.is_authenticated(try_pin):
            break
        else:
            if account.attempts >= account.max_attempts:
                print('\nYou have been locked out.')
                break

    # Manage account
    print('\n----- Manage Account -----')
    while account.access_granted:
        event = input('Do you want to "withdraw" or "exit"? ')
        if event.lower() == 'withdraw':
            account.withdraw()
        elif event.lower() == 'exit':
            print(f'\nAccount balance: ${account.balance}')
            account.reset()
            break
        else:
            print('That is not a valid answer.')

if __name__ == '__main__':
    main()