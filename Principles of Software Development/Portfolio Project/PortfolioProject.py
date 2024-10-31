import time

def validate_input(string):
    while True:
        try:
            user_input = int(input(string))
            if user_input is not ValueError:
                return user_input
        except ValueError:
            print('Enter a number')

def successful_authentication(pin):
    attempts = 0
    while True:
        authenticate = input('\nEnter your PIN: ')
        if pin == authenticate:
            return True
        else:
            attempts += 1
            print('That is the incorrect PIN.')
            print(f'Attempts: {attempts} \nAttempts remaining: {5 - attempts}')
            if attempts >= 5:
                print('You have been rejected.')
                return False

def atm_account(account_balance):
    print('Authentication Verified.')

    while True:
        print(f'\nAccount Balance: ${account_balance}')
        withdraw = validate_input('Enter how much would you like to withdraw: $')
        if withdraw > account_balance:
            print('Insufficient funds')
        else:
            account_balance -= withdraw
        print(f'\nNew account balance: ${account_balance}')
        time.sleep(1)

        if account_balance == 0:
            print('Balance is $0. Your account will be closed.')
        else:
            print('\nYou still have a positive account balance. Would you like to withdraw more?')
            resume = input('YES or NO\n>>> ')
            if resume.upper() == 'YES':
                continue
            elif resume.upper() != 'NO':
                print('Invalid response. You will be logged out.')

        return print(f'\nFinal balance: ${account_balance}')

def main():
    # Prompt user for PIN
    pin = input('Create your PIN: ')
    # account_balance = int(input('Enter your account balance: $'))
    account_balance = validate_input('Enter your account balance: $')

    # Verify identity
    if successful_authentication(pin):
        # Open account
        atm_account(account_balance)

if __name__ == '__main__':
    main()