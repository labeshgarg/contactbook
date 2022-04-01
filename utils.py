'''
This is the utility file which consists of functions to verify:-
1- Mobile number
2- Email address
3- Pin code
4- Retrieve contacts based on a search.
'''
import re 
# Verifying the mobile number
def verifyMobile(mobileNumber):
    for digit in mobileNumber:
        if not digit.isdigit():
            return False
    return len(mobileNumber) == 10  
# Verifying the pincode
def verifyPinCode(pinCode):
    for digit in pinCode:
        if not digit.isdigit():
            return False
    return len(pinCode) == 6 
# Verifying the email address
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def verifyEmail(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
# Function to return the contact based on the first and last name searches.
def getContact(firstName, lastName, contacts):
    for contact in contacts:
        if contact["First_Name"]==firstName and contact["Last_Name"]==lastName:
            return contact
    return None        

      
    
       
        