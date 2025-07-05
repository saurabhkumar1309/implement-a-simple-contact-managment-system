import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from the JSON file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts to the JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    print("Contact added successfully.\n")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print()

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter contact number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            name = input(f"Enter new name ({contacts[idx]['name']}): ") or contacts[idx]['name']
            phone = input(f"Enter new phone ({contacts[idx]['phone']}): ") or contacts[idx]['phone']
            email = input(f"Enter new email ({contacts[idx]['email']}): ") or contacts[idx]['email']
            contacts[idx] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input.\n")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            confirm = input(f"Are you sure you want to delete {contacts[idx]['name']}? (y/n): ").lower()
            if confirm == "y":
                contacts.pop(idx)
                save_contacts(contacts)
                print("Contact deleted successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input.\n")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
