from db import connect_db

def create_account():
    name = input("Enter your name:")
    balance = float(input("Enter initial deposit:"))
    #add a new account into the table
    cursor.execute("Insert into accounts (name, balance) values (%s,%s)", (name,balance))
    conn.commit()
    print("Account created!!!")


def check_balance():
    account_id = input("Enter account id:")
    #selects the balance of an account
    cursor.execute("Select balance from accounts where id =s", (account_id))
    result = cursor.fetchone()
    if results:
        print("Blance", result[0])
    else:
        print("Account not found.")

def deposit():
    account_id = input("Enter account ID:")
    amount = float(input("Enter ammount to deposit:"))
    #adding the deposited amount to the account
    cursor.execute("Update accounts set balance = balance + %s where id =s", (amount_id))
    conn.comit()
    print("Deposit succfessul")

def withdraw():
    account_id = input("Enter account od:")
    amount = float(input("Enter amount to withdraw:"))
    #Checking if the acc has enough balance
    cursor.execute("Select balance from accounts where id = %s", (account_id))
    result = cursor.fetchone()
    if result and result[0] >= amount:
        cursor.execute("Update accounts set balance = balance -%s where id %s", (amount, account_id))
        conn.comit()
        print("Withdrawl succfessul!")
    else:
        print("Insufficent funds or account not found.")

def main_menu():
    while True:
        print(" Banking Menu")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter choice (1-5):")

        if choice =="1":
            create_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice =="5":
            print("Exiting, bye!")
            break
        else:
            print("Invalid choice, try again.")
    

