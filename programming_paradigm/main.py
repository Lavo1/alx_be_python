import sys
from bank_account import BankAccount

def print_usage():
    print("Usage:")
    print("  python main-0.py balance [initial_balance]")
    print("  python main-0.py deposit <amount> [initial_balance]")
    print("  python main-0.py withdraw <amount> [initial_balance]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    operation = sys.argv[1].lower()
    initial_balance = 0.0

    if operation == "balance":
        if len(sys.argv) == 3:
            try:
                initial_balance = float(sys.argv[2])
            except ValueError:
                print("Invalid initial balance.")
                return
        account = BankAccount(initial_balance)
        account.display_balance()

    elif operation == "deposit":
        if len(sys.argv) < 3:
            print_usage()
            return
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Invalid amount.")
            return
        if len(sys.argv) == 4:
            try:
                initial_balance = float(sys.argv[3])
            except ValueError:
                print("Invalid initial balance.")
                return
        account = BankAccount(initial_balance)
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()

    elif operation == "withdraw":
        if len(sys.argv) < 3:
            print_usage()
            return
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Invalid amount.")
            return
        if len(sys.argv) == 4:
            try:
                initial_balance = float(sys.argv[3])
            except ValueError:
                print("Invalid initial balance.")
                return
        account = BankAccount(initial_balance)
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
        account.display_balance()
    else:
        print_usage()

if __name__ == "__main__":
    main()
