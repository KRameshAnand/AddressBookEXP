# This is the front end

# Import all the modules 
from AddressBookDB import *
from csv import *

# The main menu 
print("#"*80)
print("ADDRESS BOOK MENU".center(80))
print("#"*80)
print("\n")
print("What would you like to do?")
print("Press i to insert a record")
print("press v to view the records")
print("Press s to search the records by name")
print("Press c to clear all records")
print("Press d to delete records")
print("Press e to export all records to .csv file")
print("\n")
choice = input("Press the key : ")

# Input the value and call AddressBook.py fuction writeIntoDB()
if choice == "i":
	print("\n")
	try:
	    name = str(input("Enter the name : "))
	    ph_no = str(input("Enter the phone number : "))
	    email = str(input("Enter the email : "))
	except ValueError:
            print ("The values are not acceptable")
	writeIntoDB(name,ph_no,email)

# Call AddressBook.py function readIntoDB() 
elif choice == "v":
	print("\n")
	readIntoDB()

# Search AddressBook.py function searchName()
# Split names by spaces
elif choice == "s":
	print("\n")
	sname = str(input("Enter the names delimited by spaces : "))
	sname.strip()
	slst = sname.split(" ")
	for name in slst:
	    searchName(name)
#Calls clearRecords() deletes all records
elif choice == "c":
	print("\n")
	clearRecords()

elif choice == "d":
	print("\n")
	sname1 = str(input("Enter the names : "))
	sname1.strip()
	slst1 = sname1.split(" ")
	for name in slst1:
	    deleteRecords(name)

elif choice == "e":
        print("\n")
        writeCSV()
	
else:
	print("Improper Input")
