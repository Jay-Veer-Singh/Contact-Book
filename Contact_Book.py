class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name}: {contact.phone}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                search_results.append(contact)
        return search_results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if search_results:
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. {contact.name}: {contact.phone}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")
        elif choice == '5':
            index = int(input("Enter index of contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
