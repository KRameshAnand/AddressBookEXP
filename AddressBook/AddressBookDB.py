# For data base operation functions
import sqlite3

'''
This class is for database operation.



'''
class DbOp(object):

    # Constructor requires three variables name, ph_no, email
    def __init__(self, name, ph_no, email):

        self.name = name
        self.ph_no = ph_no
        self.email = email


    # Represent dbOp as name: ph_no,email
    def __repr__(self):

        print (self.name+" : "+self.ph_no+" , "+self.email)


    # Write into the data into the database
    def writeIntoDB(self):

        connd = sqlite3.connect("AddressBook.db")
        
        try:
            connd.execute('''CREATE TABLE IF NOT EXISTS ADDRESSBOOK (
                name TEXT PRIMARY KEY NOT NULL,
                ph_no TEXT NOT NULL,
                email TEXT);''')
        except Exception as e:
            print("Problem with Create Table Statement.");
 
        if self.name != "":
            connd.execute("INSERT INTO ADDRESSBOOK (name, ph_no, email) VALUES (?,?,?)",(self.name,self.ph_no,self.email))
        else:
            print("You must enter a name. ") 
        connd.commit()

        connd.close()

        
    # Read into the data in the database
    def readIntoDB(self):
        connd = sqlite3.connect("AddressBook.db")    
        print("Name".center(30),"Phone number".center(18),"Email".center(30))
        print("-"*30, "-"*18,"-"*30)
        cursor = connd.execute("SELECT * FROM AddressBook;")            
        for row in cursor:
            print("{0:30} {1:18} {2:30}".format(str(row[0]),str(row[1]),str(row[2])))
        connd.close()

    #  Search by name
    def searchName(self, nameString):
        nameString.lower()
        connd = sqlite3.connect("AddressBook.db")
        cursor = connd.execute("SELECT * FROM AddressBook WHERE name = ?",(nameString,))
        for row in cursor:
            print("{0:30} {1:18} {2:30}".format(str(row[0]),str(row[1]),str(row[2])))
        connd.close()

    # Delete some record(s) by name
    def deleteRecord(self, nameString):
        print("A L L   T H E   R E C O R D S   W I L L   B E   D E L E T E D  O F   N A M E {}",nameString.upper())
        choice = input("Are you sure to continue(y or n) : ")
        nameString.lower()
        connd = sqlite3.connect("AddressBook.db")
        connd.execute("DELETE FROM AddressBook WHERE name = ?",(nameString,))
        connd.close()
