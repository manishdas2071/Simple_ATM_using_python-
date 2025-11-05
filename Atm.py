users = {
    "Manjit": {"pin": "1302", "balance": 5000},
    "Manash": {"pin": "8812", "balance": 3000},
    "Suraj": {"pin": "9954", "balance": 8000},
    "Royel": {"pin": "4321", "balance": 8000},
    "Nabajyoti": {"pin": "9365", "balance": 8000}
}

#Validate User

# check balance

# deposit

# withdraw

# main Menu

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
