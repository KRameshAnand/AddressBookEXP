import sqlite3

def writeCSV():
    with open("Contants.csv","w") as fd:
        fd.write("Name,Phone Number,Email\n")
        connd = sqlite3.connect("AddressBook.db")
        cursor = connd.execute("SELECT * FROM AddressBook;")            
        for row in cursor:
            fd.write(str(row[1])+","+str(row[2])+","+str(row[3]))
            fd.write("\n")
