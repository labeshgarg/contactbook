'''
Program to create a contact book. the program should be able to:-
1- Add a contact.
2- Delete a contact
3- Search for a contact
4- Display all the contacts
Using a Json file to read and write data. 
'''

from storingInformation import read_contacts, write_contacts
from utils import verifyMobile, verifyPinCode, verifyEmail, getContact

FILE_LOCATION = "contacts.json"
def updateContact(contacts):
    firstName = input("Enter the first name of the contact to update: ").lower().strip()
    lastName = input("Enter the last name of the contact to update: ").lower().strip()
    contact = getContact(firstName, lastName, contacts)

    if contact:
        print("Existing contact found:")
        print(getContactName(contact))
        field = input("Which field would you like to update? (Mobile, Email_Address, Address, City, State, Pincode): ").strip()
        newValue = input(f"Enter the new value for {field}: ").strip()

        if field == "Mobile" and not verifyMobile(newValue):
            print("Invalid mobile number, please check it again.")
        elif field == "Email_Address" and not verifyEmail(newValue):
            print("Invalid email address, please check it again.")
        elif field == "Pincode" and not verifyPinCode(newValue):
            print("Invalid pincode, please check it again.")
        else:
            if field in ["City", "State", "Pincode", "Street"]:
                contact['Address'][field] = newValue
            else:
                contact[field] = newValue
            print("Contact updated successfully.")
    else:
        print("No contact found with the given name.")

# Function to ADD CONTACTS 
def addContact(contacts):
    firstName = input("Enter the first name: ").lower().strip()
    lastName = input("Enter the last name: ").lower().strip()
    mobileNumber = input("Enter the 10 digit mobile number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address: ").strip()
    city = input("Enter the city: ").lower().strip()
    state = input("Enter the state: ").lower().strip()
    pinCode = input("Enter the pin code: ").strip()

    if not firstName or not lastName:
        print("Contact must have a first and a last name.")
    elif mobileNumber and not verifyMobile(mobileNumber):
        print("Invalid mobile number, please check it again.")
    elif email and not verifyEmail(email): 
        print("Please enter a valid email addrerss.")
    elif pinCode and not verifyPinCode(pinCode):
        print("Please enter a valid pincode")
    else:
        newContact = {
            "First_Name": firstName,
            "Last_Name": lastName,
            "Mobile": mobileNumber,
            "Email_Address": email,
            "Address":{"Street":address,"City":city, "State":state, "Pincode":pinCode}
        }
        contacts.append(newContact)
        print("Contact has been added successfully. ")
        return 
    print("Invalid information, contact not added.")  

# Function to SEARCH for a contact
def searchContact(contacts):
    firstName = input("Enter the first name: ")
    lastName = input("Enter the name name: ")
    lst = []
    for contact in contacts:
        first_name = contact["First_Name"]
        last_name = contact["Last_Name"]

        if firstName not in first_name:
            continue
        if lastName not in last_name:
            continue
        lst.append(contact)
    print(f"{len(lst)} matching contacts found.")  
    displayContact(lst)  

# Function to DELETE a contact.
def deleteContact(contacts):
    firstName = input("Enter the first name: ")
    lastName = input("Enter the last name: ")
    contact  = getContact(firstName, lastName, contacts)
    if contact in contacts:
        confirmation = input("Press 'y' to confirm delete. This operation cannot be reverse.")
        if confirmation == 'y':
            contacts.remove(contact)
            print("Contact removed from the list.")
    else:
        print("No contact found.")

# Retrieving the contact in form of a string and displaying it in the display function.
def getContactName(contact):
    string = f"{contact['First_Name'].capitalize()} {contact['Last_Name'].capitalize()}"
    for items in ["Mobile", "Email_Address", "Address"]:
        value = contact[items]
        if not value:
            continue
        string += f"\n\t{items.capitalize()}: {value}"
    return string    

# Function to DISPLAY the contacts in a sorted order based on the first name.
def displayContact(contacts):
    sortedContacts = sorted(contacts, key = lambda y:y["First_Name"])
    for i , contact in enumerate(sortedContacts):
        print(f"{i+1}.{getContactName(contact)}")

# Displaying the operations.
def main(path):
    print("****CONTACT LIST****")
    print("The following operations are available:")
    print("\t1-|add|: Adding a contact.")
    print("\t2-|search|: Searching for a contact.")
    print("\t3-|delete|: Deleting a contact.")
    print("\t4-|display|: Displaying the contact list.")
    print("\t5-|update|: Updating a contact.")
    print("\t6-|q|: Press q to quit and save the contact list.")

    contacts = read_contacts(path)

    while True:
        operation = input("Please type the operation you want to perform: ").lower().strip()
        if operation == 'q':
            write_contacts(path, contacts)
            print("Contacts have been saved successfully.")
            break
        elif operation == "add":
            addContact(contacts)
        elif operation == "search":
            searchContact(contacts)   
        elif operation == "delete":
            deleteContact(contacts)
        elif operation == "display":
            displayContact(contacts)
        elif operation == "update":
            updateContact(contacts)
        else:
            print("Please enter a valid operation from the list given.")        

if __name__ == "__main__":
    main(FILE_LOCATION)