users = {
    "Manjit": {"pin": "1302", "balance": 5000},
    "Manash": {"pin": "8812", "balance": 3000},
    "Suraj": {"pin": "9954", "balance": 8000},
    "Royel": {"pin": "4321", "balance": 8000},
    "Nabajyoti": {"pin": "9365", "balance": 8000}
}

#Validate User
def validate_user(username, pin):
    if username in users and users[username]["pin"] == pin:
        return True
    return False

# check balance
def check_balance(username):
    print(f"Your current balance is ₹{users[username]['balance']}")



# deposit
def deposit(username):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount <= 0:
        print("Invalid amount.")
    else:
        users[username]["balance"] += amount
        print(f"₹{amount} deposited successfully.")
        check_balance(username)


# withdraw
def withdraw(username):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > users[username]["balance"]:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= amount
        print(f"₹{amount} withdrawn successfully.")
        check_balance(username)


# main Menu
def atm_menu(username):
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


# ATM menu
def main():
    print("=== Welcome to Python ATM ===")
    username = input("Enter username: ").lower()
    pin = input("Enter your PIN: ")

    if validate_user(username, pin):
        print(f"Login successful! Welcome, {username.title()}.")
        atm_menu(username)
    else:
        print("Invalid username or PIN. Access denied.")

if __name__ == "__main__":
    main()
