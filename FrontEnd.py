from AddressBookDB import *


print("#"*80)
print("ADDRESS BOOK MENU".center(80))
print("#"*80)
print("\n")
print("What would you like to do?")
print("Press i to insert a record")
print("press v to view the records")
print("Press s to search the records by name")
print("Press c to clear all records")
print("\n")
choice = input("Press the key : ")

if choice == "i":
	print("\n")
	name = str(input("Enter the name : "))
	ph_no = str(input("Enter the phone number : "))
	email = str(input("Enter the email : "))
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
	deleteRecord()
