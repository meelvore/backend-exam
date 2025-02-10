from domain.account import Account

class CreateNewAccount:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id: int, name: str, email: str, phone_number: int):
        account_number = f"CID{customer_id}" # Customer ID or CID
        account = Account(account_id=customer_id, customer_id=customer_id, account_number=account_number, balance=0.0)
        self.account_repository.save_account(account)
        return account