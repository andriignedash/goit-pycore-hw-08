import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def save(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.contacts, f)

    @classmethod
    def load(cls, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                contacts = pickle.load(f)
                book = cls()
                book.contacts = contacts
                return book
        except FileNotFoundError:
            return cls()

def main():
    address_book = AddressBook.load()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Remove Contact")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            address_book.add_contact(name, address)
        elif choice == "2":
            name = input("Enter name: ")
            print("Address:", address_book.get_contact(name))
        elif choice == "3":
            name = input("Enter name: ")
            address_book.remove_contact(name)
        elif choice == "4":
            address_book.save()
            print("Address book saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
