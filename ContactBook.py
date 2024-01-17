#Contact Book
#initialize a list to store your contacts, every contact is stored as a dictionary
contact_book = [
    {
      "Name":"John Doe",
      "Phone Number":"0798541872",
      "Email": "johndoe@gmail.com"
    },
]

#Add a new contact
print("Add new contact.")
def get_contact_info():
    name = input("Name:")
    phone_no = input("Phone Number:")
    email = input("Email:")
    return{"Name":name,"Phone Number":phone_no,"Email":email}

contact_info = get_contact_info()
contact_book.append(contact_info)
print(contact_book)

#Display the contacts
def display_contacts(contacts):
    print("All Contacts")
    for contact in contacts:
        print("----------")
        for key,value in contact.items():
            print(f"{key}:{value}")
    print("----------")

display_contacts(contact_book)

# #Search the contacts
# def search_contact(contact_book):
#     searched_contact = input("Search by name, email, or phone number:").lower()
#     found_contacts = []

#     for contact in contact_book:
#         for key,value in contact.items():
#             if searched_contact in value.lower():
#                 found_contacts.append(contact)

#     if found_contacts:
#         print("Found Contacts")
#         for found_contact in found_contacts:
#             print("----------")
#             for key,value in found_contact.items():
#                 print(f"{key}:{value}")
#             print("----------")
#     else:
#         print(f"Sorry, '{searched_contact}' is not in your contacts")

# search_contact(contact_book)

#Edit Contact
def edit_contact(contact_book):
    print("Edit Contact")
    contact_to_edit = input("Name, phone number or email:").lower()


    for contact in contact_book:
        for key,value in contact.items():
            if contact_to_edit in value.lower():
                print(f"Current Contact Details:\n{contact}")
               
               
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
                
                print(f"Updated Contact Details:\n{contact}")

                return [contact]
               
    
    print(f"Contact with '{contact_to_edit}' not found.")
    return []

# edited_contacts_result = edit_contact(contact_book)
# print(edited_contacts_result)
