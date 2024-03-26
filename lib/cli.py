from sqlalchemy.orm import sessionmaker
from models import engine, Contact
import shutil
import os

Session = sessionmaker(bind=engine)
session = Session()

def view_contacts():
    contacts = session.query(Contact).all()
    if contacts:
        print("ID\tName\tPhone\tEmail")
        for contact in contacts:
            print(f"{contact.id}\t{contact.name}\t{contact.phone}\t{contact.email}")
    else:
        print("No contacts found.")

def add_contact(name, phone, email, id):
    new_contact = Contact(name=name, phone=phone, email=email,id=id)
    session.add(new_contact)
    session.commit()
    print("Contact added successfully.")

def delete_contact(contact_id):
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(name):
    contacts = session.query(Contact).filter(Contact.name.like(f'%{name}%')).all()
    if contacts:
        print("Search Results:")
        print("ID\tName\tPhone\tEmail")
        for contact in contacts:
            print(f"{contact.id}\t{contact.name}\t{contact.phone}\t{contact.email}")
    else:
        print("No contacts found.")

def update_contact(contact_id, new_phone, new_email):
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.phone = new_phone
        contact.email = new_email
        session.commit()
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def backup_contacts():
    try:
        shutil.copyfile("database.db", "backup.db")
        print("Backup created successfully.")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_contacts():
    try:
        shutil.copyfile("backup.db", "database.db")
        print("Backup restored successfully.")
    except Exception as e:
        print(f"Error restoring backup: {e}")

# Main command-line interface
if __name__ == "__main__":
    while True:
        print("\nAddress Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Backup Contacts")
        print("7. Restore Contacts")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            id = input("Enter contact id")
            add_contact(name, phone, email, id)
        elif choice == "3":
            contact_id = input("Enter ID of contact to delete: ")
            delete_contact(int(contact_id))
        elif choice == "4":
            search_name = input("Enter contact name to search: ")
            search_contact(search_name)
        elif choice == "5":
            contact_id = input("Enter ID of contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            update_contact(int(contact_id), new_phone, new_email)
        elif choice == "6":
            backup_contacts()
        elif choice == "7":
            restore_contacts()
        elif choice == "8":
            print("GOODBYEE")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
