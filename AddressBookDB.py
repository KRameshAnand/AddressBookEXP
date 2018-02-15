# For data base operation functions
import sqlite3



def writeIntoDB(name,ph_no,email):

    try:
        connd = sqlite3.connect("AddressBook.db")
        connd.execute('''CREATE TABLE IF NOT EXISTS ADDRESSBOOK (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ph_no TEXT NOT NULL,
                email TEXT);''')
    except:
        print("Trouble with creation of table. \
		\nMake sure you have the apporpriate permissions");
 
    if name != "":
        connd.execute("INSERT INTO ADDRESSBOOK (name, ph_no, email)\
	 		VALUES (?,?,?)",(name,ph_no,email))
    else:
        print("You must enter a name. ") 
    
    connd.commit()
    connd.close()

        
# Read into the data in the database
def readIntoDB():

    try:     
        connd = sqlite3.connect("AddressBook.db")
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
def clearRecords():
    print("A L L   T H E   R E C O R D S   W I L L   B E   D E L E T E D")
    print("Are you sure to continue ? ")
    ch = str(input("Press y to continue or any other key to abort deleting"))
    if(ch == 'y'or ch == 'Y'):
        try:
    	    connd = sqlite3.connect("AddressBook.db")
    	    connd.execute("DELETE FROM AddressBook")
    	    connd.commit()
    	    connd.close()
        except:
            print("Database error")
