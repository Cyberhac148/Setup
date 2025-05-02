from db import connect_db

def create_account():
    name = input("Enter your name:")
    balance = float(input("Enter starting balance:"))

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("Insert into accounts (name, balance) Values(%s, %s)", (name, balance))
    db.commit()
    print("Account Created!)
    db.closse()

def check_balance():
    acc_id = input("Enter account ID:")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("Select balancd from accounts where id %s", (acc_id))
    result = cursor.fetchone()
    if result:
        print("Balance: %{result[0]}")
    else:
        print("Account not found.")
    db.close()

def deposit(): 
    acc_id = input("Enter account ID:")
    amount = float(input("Enter deposited amount:"))
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("Update accounts set balance = balance %s where id = %s", (amount, acc_id))
    db.commit()
    print("Deposit succeful.")
    db.close()

def withdraw():
    acc_id = input("Enter account ID:")
    amount = float(input("Enter withdrawl amount:"))
    db = connect_db()
    cursor = dbcursor()
    cursor.execute("Select balance from account where id =%s", (acc_id,))
    current = cursor.fetchone()
    if current and current [0] >= amount:
        cursor.execute("Update accounts set balance = balancd -%s where id = %s", (amount, acc_id))
        db.commit()
        print("Withdrawl successful.")
    else:
        print("Insufficents fund/invaild account.")
        db.close()
    
def delete_account():
    acc_id = input("Enter account ID:")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("Delete from accounts where id = %s", (acc_id))
    db.commit()
    print("Account deleted.")
    db.close()

def menu():
    while True:
        print("    Banking System     ")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Choose an option:")
        if choice == "1":
            create_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            print("Good bye! Have a good day!")
            break
        else:
            print("Invalid choice, Try again.")

if __name__ =="__main__":
    menu()
