import mysql.connector as mc

class Account:
    def db_connection():
        mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bank"
        )
        mycursor = mydb.cursor()
    
    def insert_account_info():
        