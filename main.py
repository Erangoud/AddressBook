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
        return (f'{self.name},{self.address},{self.city},{self.state},{self.zip},{self.phoneno},{self.email}')


class AddressBookMain:  # use case 1
    contacts = {}  # Store contacts in a dictionary

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
        new_contact = Contact(name, address, city, state, zip, phoneno, email)
        self.contacts[name] = new_contact  # Add the contact to the dictionary with name as the key

    @staticmethod
    def view_all_contacts():
        print('All contacts:')
        for name, contact in AddressBookMain.contacts.items():
            print(contact)

    def display_contacts(self):
        print("specified Contact details:")
        for name, contact in self.contacts.items():
            print(f'[Name: {name}, Address: {contact.address}]')



ob1=AddressBookMain()
ob2=AddressBookMain()
ob1.add_contacts()
ob2.add_contacts()
# ob1.display_contacts()
AddressBookMain.view_all_contacts()


