contacts = {}

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully")

    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            for name, info in contacts.items():
                print("Name:", name)
                print("Phone:", info["phone"])
                print("Email:", info["email"])
                print("-----")

    elif choice == "3":
        name = input("Enter name to edit: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
