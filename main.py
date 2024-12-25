class Contact:  # use case 2
    def __init__(self, name, address, city, state, zip, phoneno, email):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phoneno = phoneno
        self.email = email

    def __str__(self):
        return (f'[{self.name},{self.address},{self.city},{self.state},{self.zip},{self.phoneno},{self.email}]')


class AddressBookMain:  # use case 1
    address_books = {}  # Dictionary of Address Book Name to Address book 

    def __init__(self):
        print("Welcome to AddressBook program")

    def create_address_book(self):  # use case 6
        """Each Address Book has a unique Name"""
        name = input('Enter a unique name for the new address book: ')
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            self.address_books[name] = {}  # Create a new, empty address book
            print(f"Address book '{name}' created successfully.")

    def add_contacts(self):  # use case 2
        address_book_name = input('Enter the name of the address book to add contact to: ')
        if address_book_name not in self.address_books:
            print(f"Address book '{address_book_name}' does not exist. Create it first.")
            return
        contacts = self.address_books[address_book_name]  # Access the specific address book
    
        name = input('name: ')
        address = input('address: ')
        city = input('city: ')
        state = input('state: ')
        zip = input('zip: ')
        phoneno = input('phoneno: ')
        email = input('email: ')
        if name in contacts:
            print(f"Contact with name {name} already exists in address book '{address_book_name}'.")
        else:
            new_contact = Contact(name, address, city, state, zip, phoneno, email)
            contacts[name] = new_contact
            print(f"Contact '{name}' added successfully to address book '{address_book_name}'.")

    @staticmethod
    def view_all_contacts():
        print('All contacts across all address books:')
        for address_book, contacts in AddressBookMain.address_books.items():
            print(f"Address Book: {address_book}")
            for name, contact in contacts.items():
                print(f"  {name}: {contact}")

    def edit_contact(self):  # use case 3
        address_book_name = input('Enter the name of the address book: ')
        if address_book_name not in self.address_books:
            print(f"Address book '{address_book_name}' does not exist.")
            return
        contacts = self.address_books[address_book_name]

        name = input('Enter the name of the contact to edit: ')
        if name in contacts:
            print(f"Editing contact: {contacts[name]}")
            address = input('New address (press Enter to skip): ') or contacts[name].address
            city = input('New city (press Enter to skip): ') or contacts[name].city
            state = input('New state (press Enter to skip): ') or contacts[name].state
            zip = input('New zip (press Enter to skip): ') or contacts[name].zip
            phoneno = input('New phoneno (press Enter to skip): ') or contacts[name].phoneno
            email = input('New email (press Enter to skip): ') or contacts[name].email
            contacts[name] = Contact(name, address, city, state, zip, phoneno, email)
            print(f"Contact updated successfully: {contacts[name]}")
        else:
            print(f"No contact found with the name {name}..")

    def del_contact(self):  # use case 4
        address_book_name = input('Enter the name of the address book: ')
        if address_book_name not in self.address_books:
            print(f"Address book '{address_book_name}' does not exist.")
            return
        contacts = self.address_books[address_book_name]

        name = input('Enter the name of the contact to delete: ')
        if name in contacts:
            del contacts[name]
            print(f"The contact '{name}' has been deleted from address book '{address_book_name}'.")
        else:
            print(f"The contact name '{name}' does not exist in address book '{address_book_name}'.")

    def view_all_address_books(self):  # UC5
        print("All address books:")
        for name in self.address_books.keys():
            print(f"- {name}")



ob = AddressBookMain()
while True:
    print("\nMenu:")
    print("1. Create Address Book")
    print("2. Add Contact to Address Book")
    print("3. View All Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. View All Address Books")
    print("7. Exit")

    #add multiple Address Book to the System
    choice = input("Enter your choice: ")
    if choice == '1':
        ob.create_address_book()
    elif choice == '2':
        ob.add_contacts()
    elif choice == '3':
        AddressBookMain.view_all_contacts()
    elif choice == '4':
        ob.edit_contact()
    elif choice == '5':
        ob.del_contact()
    elif choice == '6':
        ob.view_all_address_books()
    elif choice == '7':
        print("Exiting Address Book program Thankyou.")
        break
    else:
        print("Invalid choice. Please try again.")
