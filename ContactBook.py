#Contact Book
#initialize a list to store your contacts, every contact is stored as a dictionary
import json
contact_book = [
    {
      "Name":"John Doe",
      "Phone Number":"0798541872",
      "Email": "johndoe@gmail.com"
    },
]


#Add a new contact
def get_contact_info():
    print("Add new contact.")
    name = input("Name:")
    phone_no = input("Phone Number:")
    email = input("Email:")
    return{"Name":name,"Phone Number":phone_no,"Email":email}


#Display the contacts
def display_contacts(contacts):
    print("All Contacts")
    for contact in contacts:
        print("----------")
        for key,value in contact.items():
            print(f"{key}:{value}")
    print("----------")


#Search the contacts
def search_contact(contact_book):
    searched_contact = input("Search by name, email, or phone number:").lower()
    found_contacts = set()

    for contact in contact_book:
        for key,value in contact.items():
            if searched_contact in value.lower():
                found_contacts.add(tuple(contact.items()))

    if found_contacts:
        print("Found Contacts")
        for found_contact in found_contacts:
            print("----------")
            for key,value in dict(found_contact).items():
                print(f"{key}:{value}")
            print("----------")
    else:
        print(f"Sorry, '{searched_contact}' is not in your contacts")


#Edit Contact
def edit_contact(contact_book):
    print("Edit Contact")
    contact_to_edit = input("Name, phone number or email:").lower()

    for contact in contact_book:
        for key,value in contact.items():
            if contact_to_edit in value.lower():
                print(f"Current Contact Details:")
                print("----------")
                print(f"Name: {contact['Name']}")
                print(f"Phone Number: {contact['Phone Number']}")
                print(f"Email: {contact['Email']}")
                print("----------")
               
                prompt = '''
                1)Edit name
                2)Edit Phone Number
                3)Edit Email
                '''
                print(prompt)
                user_choice=int(input("Enter your choice(1,2 or 3):"))
                if user_choice == 1:
                    new_name=input("Enter new name:")
                    contact["Name"] = new_name
                elif user_choice == 2:
                    new_phoneNo = input("Enter new phone number:")
                    contact["Phone Number"] = new_phoneNo
                elif user_choice == 3:
                    new_email = input("Enter new email:")
                    contact["Email"] = new_email
                else:
                    print("Invalid Input")
                
                print(f"Updated Contact Details:")
                print("----------")
                print(f"Name: {contact['Name']}")
                print(f"Phone Number: {contact['Phone Number']}")
                print(f"Email: {contact['Email']}")
                print("----------")
                return [contact]
               
    
    print(f"Contact with '{contact_to_edit}' not found.")
    return []

#Delete Contact
def delete_contact(contact):
    contact_to_delete = input("Enter Contact to delete(name, phone number or email):").lower()

    for contact in contact_book:
        for key, value in contact.items():
            if contact_to_delete in value.lower():
                contact_book.remove(contact)
                print(f"Successfully deleted '{value}'")
                display_contacts(contact_book)
                return

    print(f"Contact with '{contact_to_delete}' not found.")
    print("Remaining contacts:")
    display_contacts(contact_book)

#Saving the contact to a file
def save_contacts_to_file(contacts ,filename = "contact_book.json"):
    try:
        with open(filename, "w") as file:
            json.dump(contacts, file, indent=2)
        print(f"Contacts succesfully saved to {filename}")
    except Exception as e:
        print(f"Error: Unable to save contact to {filename}.Reason:{e}")

# Function to load contacts from a file
def load_contacts_from_file(filename="contact_book.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#Load contacts at program start
contact_book = load_contacts_from_file()

while True:
    action = int(input('''
        Enter Option.
        1)Add Contact(s)
        2)Display the Contacts
        3)Search Contact(s)
        4)Edit Contact(s)
        5)Delete contact(s)
        6)Exit
        ----->
        '''))

    if action == 1:
        contact_info = get_contact_info()
        contact_book.append(contact_info)
        print("Contact added successfully.")
        display_contacts(contact_book)
        
    elif action == 2:
        display_contacts(contact_book)

    elif action == 3:
        search_contact(contact_book)

    elif action == 4:
        edit_contact(contact_book)

    elif action == 5:
        delete_contact(contact_book)

    elif action == 6:
        print("Exiting...Goodbye:)")
        save_contacts_to_file(contact_book)
        break
    else:
        print("Invalid choice")
   


