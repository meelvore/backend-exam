class GenerateAccountStatement:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id: int):
        account = self.account_repository.find_account_by_id(account_id)
        statement = account.generate_account_statement()
        return statement