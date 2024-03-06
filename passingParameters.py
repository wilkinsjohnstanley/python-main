#sumlate a bank. Deposit/withdrawal transactions

#create a class 
class BankAccount:
    #init method
    #bal comes fromo the outside code
    def __init__(self, bal):
        self.balance = bal
    #create a deposit method
    def deposit(self, amount):
        self.balance+=amount
    #create a withdrawal method
    def withdrawal(self,amount):
        if self.balance>=amount:
            self.balance -=amount
        else:
            print('Not enough fund for withdrawal')
    #check balance

    def get_balance(self):
        return self.balance
def main():
    starting_balance=float(input('Enter starting balance: $'))
    #create object(instance)
    savings=BankAccount(starting_balance)
    #deposit a check
    deposit_check=float(input('How much is your deposit?: $'))
    print('Amount to be despoited: ', deposit_check)
    savings.deposit(deposit_check)

    #display balance
    print(f'Your current balance is ${savings.get_balance():0.2f}')

    #make withdrawal
    cash=float(input('How much do you want to withdrawal?: $'))
    print('Amount being withdrawan: $', cash)
    savings.withdrawal(cash)
    #display balance
    print(f'Your current balance is: ${savings.get_balance():0.2f}')

main()