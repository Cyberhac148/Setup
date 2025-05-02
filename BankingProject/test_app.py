from db import connect_db

def test_create_account():
    #Testing the accoun creation
    db = connect_db()
    cursor = db.cursor()

    #Creating a test by checking user
    cursor.execute("Insert into accounts(name, balance) Values (%s,%s)",("Test User", 100.0))
    #Here I am getting the last inserted account id
    cursor.execute("Select id from accounts where name =%s", ("Test User",))
    result = cursor.fetchone()

    #asserting that the account id exists and is vaild
    assert result and isinstance(result[0], int), "Account creation failed or invalid ID."

    print("test_create_account passed.")
    db.close()

def run_test():
    test_create_account()

if __name__ =="__main__":
    run_test()

