class Account:     
    def __init__(self, owner , balance =0 ):
        self.owner = owner 
        self.balance = balance

    def deposit(self, anount):
        if anount >0:
            self.balance +=anount
            print({anount , self.balance})
        else:
            print("No money on deposit")

    def withdraw(self ,anount):
        if anount >self.balance:
            print(self.balance)
        elif anount >0 :
            self.balance -= anount
            print(self.balance , anount)
    
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")