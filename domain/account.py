class Account:
    def __init__(self, account_id: int, customer_id: int, account_number: str, balance: float = 0.0):
        self.transactions = []  # for storing transaction history

        self.account_id = account_id 
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        

    # Adds money to the account balance
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount is invalid")
        self.balance += amount
        self.transactions.append(f"Deposited {amount}. New balance: {self.balance}")
        return f"Deposit Successful! Your new balance is {self.balance}"

    # Withdraws money from the account
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal")
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}. New balance: {self.balance}")
        return f"Withdrawal Successful. Your new balance is {self.balance}"
        
    def generate_account_statement(self):
        return "\n".join(self.transactions) if self.transactions else "No transactions available."