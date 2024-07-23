import mysql.connector


class DatabaseConnection:
    def _init_(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="advance_python"
        )
        self.cursor = self.connection.cursor()


class banker:

    def register():
        # INSERT INTO Banker (username, password) VALUES ('banker_username', 'banker_password');

    def login():
        # SELECT * FROM Banker WHERE username = 'banker_username' AND password = 'banker_password';

    def update_customers():
        # UPDATE Customer SET column1 = value1, column2 = value2 WHERE banker_id = 'banker_id';

    def view_customers():
        # SELECT * FROM Customer WHERE banker_id = 'banker_id';

    def delete_customers():
        # DELETE FROM Customer WHERE banker_id = 'banker_id';

        
class Customer:

    def register():
        # INSERT INTO Customer (banker_id, username, password) VALUES ('banker_id', 'customer_username', 'customer_password');

    def login():
        # SELECT * FROM Customer WHERE username = 'customer_username' AND password = 'customer_password';

    def withdraw_amount():
        # UPDATE Customer SET balance = balance - withdrawal_amount WHERE customer_id = 'customer_id';
    
    def deposit_amount():
        # UPDATE Customer SET balance = balance + deposit_amount WHERE customer_id = 'customer_id';
    
    def view_balance():
        # SELECT balance FROM Customer WHERE customer_id = 'customer_id';

while True:
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            
            banker_menu()
        elif choice == "2": 
            customer_menu()
        elif choice == "3": 
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def banker_menu():
    pass

def customer_menu():
    pass