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
    contacts = {}  

    def __init__(self):
        print("Welcome to AddressBook program")

    def add_contacts(self):  # use case 2
        name = input('name :')
        address = input('address :')
        city = input('city :')
        state = input('state :')
        zip = input('zip :')
        phoneno = input('phoneno :')
        email = input('email :')
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        else:
            new_contact = Contact(name, address, city, state, zip, phoneno, email)
            self.contacts[name] = new_contact  # Adding the contact to the dictionary with name as the key

    @staticmethod
    def view_all_contacts():
        print('All contacts:')
        for name, contact in AddressBookMain.contacts.items():
            print(f'{name}:{contact}')

    
    def edit_contact(self):  # use case 3
        name = input('Enter the name of the contact to edit: ')
        if name in self.contacts:
            print(f"Editing contact: {self.contacts[name]}")
            address = input('New address (press Enter to skip): ') or self.contacts[name].address
            city = input('New city (press Enter to skip): ') or self.contacts[name].city
            state = input('New state (press Enter to skip): ') or self.contacts[name].state
            zip = input('New zip (press Enter to skip): ') or self.contacts[name].zip
            phoneno = input('New phoneno (press Enter to skip): ') or self.contacts[name].phoneno
            email = input('New email (press Enter to skip): ') or self.contacts[name].email
            self.contacts[name] = Contact(name, address, city, state, zip, phoneno, email)
            print(f"Contact updated successfully: {self.contacts[name]}")
        else:
            print(f"No contact found with the name {name}.")



ob1=AddressBookMain()
ob1.add_contacts()
AddressBookMain.view_all_contacts()
ob1.edit_contact()

