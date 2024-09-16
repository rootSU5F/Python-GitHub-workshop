contacts = {}

def addContact():
    name = input("Enter the name: \n")
    phone = input("Enter the phone: \n")
    email = input("Enter the email: \n")
    if name in contacts:
        print("This contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("The contact has been added successfully!")

def updateContact():
    print("\n----------------------\nUpdating Contact...\n----------------------")
    name = input("Enter the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone: ")
        email = input("Enter the new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("The contact has been updated successfully!")
    else:
        print("This contact doesn't exist!")

def deleteContact():
    name = input("Enter the name: ")
    if name in contacts:
        del contacts[name]
        print("The contact has been deleted successfully!")
    else:
        print("This contact doesn't exist!")

def viewContacts():
    if contacts:
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("-" * 20, "\n")
    else:
        print("No contacts available!")

while True:
    print("Contact Management System\n"
          "----------------------------\n"
          "1. Add Contact\n"
          "2. Update Contact\n"
          "3. Delete Contact\n"
          "4. View Contacts\n"
          "5. Exit\n"
          "----------------------------")
    user_input = int(input("Please enter your choice: "))

    if user_input == 1:
        addContact()
    elif user_input == 2:
        updateContact()
    elif user_input == 3:
        deleteContact()
    elif user_input == 4:
        viewContacts()
    elif user_input == 5:
        print("Exiting the system. Goodbye!")
        break  # This will exit the while loop and end the program
    else:
        print("Invalid option! Please enter a number between 1 and 5.")
