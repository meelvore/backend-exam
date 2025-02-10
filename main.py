from infrastructure.accountRepository import AccountRepository
from use_case.createNewAccount import CreateNewAccount
from use_case.generateAccountStatement import GenerateAccountStatement
from use_case.makeTransaction import MakeTransaction

if __name__ == "__main__":
    # Initialize Account Repository
    account_repository = AccountRepository()

    # Use Case: Create a new account
    create_account_use_case = CreateNewAccount(account_repository)
    account = create_account_use_case.create_account(customer_id=4321, name="John Doe", email="john@email.com", phone_number=9912345678)

    print(f"New Bank Account Created: {account.account_number}")

    # Use Case: deposit()
    transaction_use_case = MakeTransaction(account_repository)
    transaction_use_case.make_transaction(account.account_id, 500, "deposit")
    print(f"\nAfter deposit: {account.generate_account_statement()}")

    # Use Case: withdraw()
    transaction_use_case.make_transaction(account.account_id, 200, "withdraw")
    print(f"\nAfter withdrawal: {account.generate_account_statement()}")

    # Use Case: Generate account statement
    statement_use_case = GenerateAccountStatement(account_repository)
    print("\nAccount Statement:\n", statement_use_case.generate_account_statement(account.account_id))
