from AddressBookDB import *
from csv import *


print("#"*80)
print("ADDRESS BOOK MENU".center(80))
print("#"*80)
print("\n")
print("What would you like to do?")
print("Press i to insert a record")
print("press v to view the records")
print("Press s to search the records by name")
print("Press c to clear all records")
print("Press e to export all records to .csv file")
print("\n")
choice = input("Press the key : ")

if choice == "i":
	print("\n")
	try:
	    name = str(input("Enter the name : "))
	    ph_no = str(input("Enter the phone number : "))
	    email = str(input("Enter the email : "))
	except ValueError:
            print ("The values are not acceptable")
	writeIntoDB(name,ph_no,email)

elif choice == "v":
	print("\n")
	readIntoDB()

elif choice == "s":
	print("\n")
	sname = str(input("Enter the name : "))
	searchName(sname)

elif choice == "c":
	print("\n")
	clearRecords()

elif choice == "e":
        print("\n")
        writeCSV()
