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
    address_book_city={}
    address_book_state={}
    def __init__(self):
        print("Welcome to AddressBook program")

    def create_address_book(self):  # use case 5/6
        name = input('Enter a unique name for the new address book: ')
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            self.address_books[name] = {}  
            print(f"Address book '{name}' created successfully.")

    def add_contacts(self):  # use case 2
        address_book_name = input('Enter the name of the address book to add contact to: ')
        if address_book_name not in self.address_books:
            print(f"Address book '{address_book_name}' does not exist. Create it first.")
            return
        contacts = self.address_books[address_book_name] 
    
        name = input('name: ')
        address = input('address: ')
        city = input('city: ')
        state = input('state: ')
        zip = input('zip: ')
        phoneno = input('phoneno: ')
        email = input('email: ')
        if name in contacts: # use case 7 Ability to ensure there is no Duplicate Entry of the same Person in a particular Address Book
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

    def view_all_address_books(self):  # use case 5
        print("All address books:")
        for name in self.address_books.keys():
            print(f"- {name}")

    def search_person_by_city_or_state(self): # use case 8
        criteria = input("search by 'city' or 'state':")
        if criteria != 'city' and criteria != 'state':
            print('invalid choice . select either "city" or "state" ')
            return
        search_value=input(f"enter the {criteria} to search : ")
        print(f"searching for contacts by {criteria}:{search_value}")

        found=False # a flag 
        for addressbook,contacts in self.address_books.items():
            for name,contact in contacts.items():
                if (criteria=='city' and contact.city==search_value) or (criteria=='state' and contact.state==search_value):
                    print(f"found in address book '{addressbook}':{contact}")
                    found=True
        if not found:
            print(f"no contacts found for {criteria}'{search_value}")


    def view_persons_by_city_or_state(self):  # use case 9
        criteria = input("View persons by 'city' or 'state': ")
        if criteria not in ['city', 'state']:
            print("Invalid choice. Select either 'city' or 'state'.")
            return
        store = self.address_book_city if criteria == 'city' else self.address_book_state
        store.clear()

                
        for addressbook,contacts in self.address_books.items():
            for name,contact in contacts.items():
                key=contact.city if criteria=='city' else contact.state
                
                if key not in store:
                    store[key]=[]
                store[key].append(contact)

        for key,persons in store.items():
                print(f'{criteria}:{key}')
                for person in persons:
                    print(f'{person}')

    def count_by_city_or_state(self): #use case 10 
        criteria=input("count persons by city or state ")
        if criteria not in ['city','state']:
            print("invalid choice. select either 'city' or 'state' ")
            return 
        count={}
        for addressbook,contacts in self.address_books.items():
            for name,contact in contacts.items():
                key=contact.city if criteria=='city' else contact.state
                if key not in count:
                    count[key]=0
                count[key] +=1

        for key,number in count.items():
            print(f"city:{key} :--> The total no.of persons found are :{number}")
                    

    def sort_contacts_by_name(self):
        book_name=input("enter the address book name to sort :")
        if book_name not in self.address_books:
            print(f"The addressbook {book_name} doesn't exists ")
            return
        contacts=self.address_books[book_name]
        if not contacts:
            print(f"Address book '{book_name}' has no contacts to sort.")
            return
        sorted_contacts=sorted(contacts.items(),key=lambda x :x[0])
        print(type(sorted_contacts))
        print(f"This are the sorted contacts  :")
        for  name,contacts in  sorted_contacts:
            print(contacts)



ob = AddressBookMain()

while True:
    print("\nMenu:")
    print("1. Create Address Book")
    print("2. Add Contact to Address Book")
    print("3. View All Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. View All Address Books")
    print("7. search person by city or state")
    print("8. view person by city or state")
    print("9.Count persons by city or state ")
    print("10. sort contacts by name")
    print("11. Exit")

    #add multiple Address Book and contacts to the System :- use case 5
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
        ob.search_person_by_city_or_state()
    elif choice == '8':
        ob.view_persons_by_city_or_state()
    elif choice == '9':
        ob.count_by_city_or_state()
    elif choice == '10':
        ob.sort_contacts_by_name()
    elif choice == '11':
        print("Exiting Address Book program Thankyou.")
        break
    else:
        print("Invalid choice. Please try again.")
