# For data base operation functions
import sqlite3



def writeIntoDB(name,ph_no,email):

    connd = sqlite3.connect("AddressBook.db")
        
    try:
        connd.execute('''CREATE TABLE IF NOT EXISTS ADDRESSBOOK (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ph_no TEXT NOT NULL,
                email TEXT);''')
    except Exception as e:
        print("Problem with Create Table Statement.");
 
    if name != "":
        connd.execute("INSERT INTO ADDRESSBOOK (name, ph_no, email) VALUES (?,?,?)",(name,ph_no,email))
    else:
        print("You must enter a name. ") 
    
    connd.commit()
    connd.close()

        
# Read into the data in the database
def readIntoDB():

    connd = sqlite3.connect("AddressBook.db")

    try:    
        print("{0:3} {1:30} {2:14} {3:30}".format("ID","Name","Phone Number","Email"))
        print("-"*3,"-"*30, "-"*14,"-"*30)
        cursor = connd.execute("SELECT * FROM AddressBook;")            
        for row in cursor:
            print("{0:3} {1:30} {2:14} {3:30}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3])))
    except:
        print("Error with database")
   
    connd.close()

#  Search by name
def searchName(nameString):
    try:
        connd = sqlite3.connect("AddressBook.db")
        cursor = connd.execute("SELECT * FROM AddressBook WHERE name = ?",(nameString,))
        for row in cursor:
            print("{0:3} {1:30} {2:14} {3:30}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3])))
    except:
        print("Error with database")
    connd.close()

# Delete some record(s) by name
def deleteRecord():
    print("A L L   T H E   R E C O R D S   W I L L   B E   D E L E T E D")
    connd = sqlite3.connect("AddressBook.db")
    connd.execute("DELETE FROM AddressBook")
    connd.commit()
    connd.close()
