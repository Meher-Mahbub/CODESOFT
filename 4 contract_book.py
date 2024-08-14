def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contacts(contacts):
    print("\nContact List:")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    print("\nSearch Contact")
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("No contact found.")

def update_contact(contacts):
    print("\nUpdate Contact")
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Current details - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    print("\nDelete Contact")
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
