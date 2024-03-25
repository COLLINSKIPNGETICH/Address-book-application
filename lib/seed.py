from sqlalchemy.orm import sessionmaker
from models import engine, Contact

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    contacts = [
        {"name": "Amos kip", "phone": "0750349450", "email": "amos@gmail.com"},
        {"name": "Jane Smith", "phone": "0758913660", "email": "jane@gmail.com"},
        {"name": "Alice Johnson", "phone": "011553345", "email": "alice@gmail.com"},
    ]

    for contact_data in contacts:
        contact = Contact(**contact_data)
        session.add(contact)

    session.commit()
    print("Seed data added successfully.")

if __name__ == "__main__":
    seed_data()
