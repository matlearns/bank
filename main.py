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
            if not all(word.isalpha() for word in name.split()): #note copy maa saarne
                raise ValueError("Name must contain alphabet") 
            sex = input("Input gender Male, Female, and Other as M, F, or O: ")
            if not sex in ['M', 'F', 'O']: #note copy maa saarne
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
        try:        
            account_no = int(input("Input account: "))
            if not account_no:
                raise ValueError("The field must filled with proper ac number.")
            deposit_amount = float(input("Amount to save: "))
            if not deposit_amount:
                raise ValueError("The field must filled with proper ac number.")
            
            #fetch all credit
            check_cr = "SELECT Cr FROM a_customer_info WHERE account_no = %s"
            value = (account_no, )
            self.mycursor.execute(check_cr, value)
            all_cr = self.mycursor.fetchall()
            total_cr = 0
            for x in all_cr:
                total_cr += x[0] #yo note garne
           
            #fetch all credit
            check_dr = "SELECT Dr FROM a_customer_info WHERE account_no = %s"
            value = (account_no, )
            self.mycursor.execute(check_dr, value)
            all_dr = self.mycursor.fetchall()
            total_dr = 0
            for x in all_dr:
                total_dr += x[0] #yo note garne
           
            current_saving = float(total_cr - total_dr)
           
            sql = "UPDATE a_customer_info SET Cr = %s, Dr = 0 WHERE account_no = %s"
            values= (deposit_amount, account_no)

            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print(f"Successfully NRs. {deposit_amount} deposited to account # {account_no}. Your updated balance is NRs. {current_saving+deposit_amount}.")
        
        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()
    
    def withdraw(self):
        try:        
            account_no = int(input("Input account: "))
            if not account_no:
                raise ValueError("The field must filled with proper ac number.")
            withdraw_amount = float(input("Amount to withdraw: "))
            if not withdraw_amount:
                raise ValueError("The field must filled with proper ac number.")
            
            #fetch all credit
            check_cr = "SELECT Cr FROM a_customer_info WHERE account_no = %s"
            value = (account_no, )
            self.mycursor.execute(check_cr, value)
            all_cr = self.mycursor.fetchall()
            total_cr = 0
            for x in all_cr:
                total_cr += x[0] #yo note garne
           
            #fetch all credit
            check_dr = "SELECT Dr FROM a_customer_info WHERE account_no = %s"
            value = (account_no, )
            self.mycursor.execute(check_dr, value)
            all_dr = self.mycursor.fetchall()
            total_dr = 0
            for x in all_dr:
                total_dr += x[0] #yo note garne
           
            current_saving = float(total_cr - total_dr)

            if current_saving >= withdraw_amount:
                sql = "UPDATE a_customer_info SET Dr = %s, Cr = 0 WHERE account_no = %s" #yahaa Cr = 0  set gardaa individual transaction create hunchha, natra khaali dr maa update hunchha
                values= (withdraw_amount, account_no)

                self.mycursor.execute(sql, values)
                self.mydb.commit()
                print(f"Successfully NRs. {withdraw_amount} withdrew from to account # {account_no}. Your updated balance is NRs. {current_saving-withdraw_amount}.")
            else:
                raise ValueError("Insufficient balance.")
        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()

    def transaction_statement(self):
        print("Yasko kaam garna baanki chha: ")
        account_number = input("Account Number: ")
        sql = "SELECT date_and_time, Cr, Dr FROM a_customer_info WHERE account_no = %s"
        value = (account_number, ) #it must be tuple
        self.mycursor.execute(sql, value)
        result = self.mycursor.fetchall()
        for i in result:
            print(i)
    
    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()

account = Account()
action = int(input("Select 1 or 2 or 3 or 4 or 5 or 6 for new account opening, existing account update, check account information, deposit, withdraw, and view statement: "))
if action == 1:
    account.open_account()
elif action == 2: 
    account.update_account()
elif action == 3:
    account.view_account()
elif action == 4:
    account.deposit()
elif action == 5:
    account.withdraw()
elif action == 6:
    account.transaction_statement()        
else:
    raise ValueError("Enter proper number.")
account.close_connection()