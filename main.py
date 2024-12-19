
class Contact: #use case 2
    def __init__(self,name,address,city,state,zip,phoneno,email):
        self.name=name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phoneno=phoneno
        self.email=email

    def __str__(self):
        return (f'{self.name},{self.address},{self.city},{self.state},{self.zip},{self.phoneno},{self.email}')

class AddressBookMain: #use case 1
    # contacts=[]
    def __init__(self):
        print("Welcome to AddressBook program ")

ob1=AddressBookMain() 