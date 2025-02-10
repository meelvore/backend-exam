class AccountRepository:
    def __init__(self):
        self.accounts = {} # store account here

    def save_account(self, account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id: int):
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id: int):
        return [account for account in self.accounts.values() if account.customer_id == customer_id]