from mongoengine import disconnect

from models import Contacts

from faker import Faker

fake = Faker()


def seed_contacts():
    contacts_list = []
    for i in range(25):
        contact = Contacts(
            fullname=fake.name(), number=fake.phone_number(), email=fake.email()
        )
        contacts_list.append(contact)
        contact.save()
    return contacts_list


if __name__ == "__main__":
    seed_contacts()
    disconnect()
