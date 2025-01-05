#Bank Account Manager Program

class Bankaccount:
    def __init__(self, name, acc_number, balance = 0):
        self.__name = name
        self.__balance = balance
        self.__acc_number = acc_number
        self.transactios = []
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        try:
            if amount <=0:
                raise ValueError("Deposit amount must be positive.")
            self.__balance += amount
            self.transactios.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def withdraw(self, amount):
        try:
            if amount > self.__balance:
                raise ValueError("Insufficient balance.")
            if amount <=0:
                raise ValueError("Withdraw amount must be positive.")
            self.__balance -= amount
            self.transactios.append(f"Withdraw: ${amount}")
            print(f"${amount} withdrawn succeffully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def balance_inquiry(self):
        return f"your current balance is: ${self.__balance}"

    def transaction_history(self):
        if not self.transactios:
            return "No transaction found."
        return "\n".join(self.transactios)
    
    # Operator overloading for string representation
    def __str__(self):
        return (f"Account Number: {self.__acc_number}\n"
                f"Cuctomer Nmae: {self.__name}\n"
                f"Balance: ${self.__balance}")