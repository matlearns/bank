import mysql.connector as mc

class Account:
    def __init__(self):
        self.mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bank"
        )
        self.mycursor = self.mydb.cursor()        
    
    def open_account(self):
        try:
            name = input("Type name: ").strip()
            if not name:
                raise ValueError("Name field must be filled with alphabet.")
            if not all(word.isalpha() for word in name.split()): #??? how this line works
                raise ValueError("Name must contain alphabet") 
            sex = input("Input gender Male, Female, and Other as M, F, or O: ")
            if not sex in ['M', 'F', 'O']: #practice how this list work
                raise ValueError("Must choose a proper gender")
            address = input("Type address: ").strip()
            if not address:
                raise ValueError("Address must filled")
            contact = input("Type contact: ").strip()
            if not contact.isnumeric() and len(contact) != 10:
                raise ValueError("Contact must be 10 digit number")
            
            sql = "INSERT INTO customer_info (name, address, contact, sex) VALUES (%s, %s, %s, %s)"
            values = (name, address, contact, sex)
            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print(f"Successfully account created for {name}.")
        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()

    def update_account(self): #Remain to work to reduce security risks.
        account_number = input("Which account number do you want to change: ")
        change_column = input("Type name or address or contact or sex to update Name, Address, Contact, and Sex: ")
        change_value = input(f"Type the {change_column} of account number {account_number} to change: ")
        sql = f"UPDATE customer_info SET {change_column} = %s WHERE account_no = %s"
        values = (change_value, account_number)
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print(f"Successfully {change_column} updated to {change_value} of account number {account_number}.") 

    def view_account(self): #Remain to work to reduce security risks.
        account_query = input("account_no to search by Account Number and contact to search by Contact: ")
        query_value = input(f"Type the value of {account_query}: ")
        sql = f"SELECT * FROM customer_info WHERE {account_query} = %s"
        value = (query_value, ) #it must be tuple
        self.mycursor.execute(sql, value)
        result = self.mycursor.fetchall()
        for i in result:
            print(i)
        self.mydb.commit()

    def deposit(self):
        account_no = int(input("Input account: "))
        deposit_amount = int(input("Amount to save: "))
        """Logic: 
        - go to the account number 'x'.
        - add 'a' amount to the 'x' account.
        - in next deposit, add 'b' amount to the 'x' account.
        """
    def withdraw(self):
        beneficary_account_no = int(input("Input account: "))
        withdraw_amount = int(input("Amount to withdraw: "))    
        
    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()

account = Account()
action = int(input("Select 1 or 2 or 3 for new account opening, existing account update, and check account information: "))
if action == 1:
    account.open_account()
elif action == 2: 
    account.update_account()
elif action == 3:
    account.view_account()

account.close_connection()