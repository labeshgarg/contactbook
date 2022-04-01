'''
This is the file which consists of functions to read and 
write the data into the json file.
'''

import json

# Reading the contacts from the json file.
def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []
    return contacts

# Writing the contacts into the json file
def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)