from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Base, Factory, Manager, Employee, Shift
from datetime import datetime
import random
import os

# Create an SQLAlchemy engine to interact with the database
engine = create_engine('sqlite:///factory_data.db')

# Check if the database file exists
if not os.path.exists('factory_data.db'):
    print("Database file 'factory_data.db' does not exist. Please create it.")
    exit()

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a Faker instance
fake = Faker()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def create_fake_factories(num_factories=1000):
    for _ in range(num_factories):
        factory = Factory(
            location=fake.city(),
            type=fake.word()
        )
        session.add(factory)
    session.commit()

def create_fake_managers(num_managers=1000):
    factories = session.query(Factory).all()
    for _ in range(num_managers):
        factory = random.choice(factories)
        manager = Manager(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=random.choice(['Male', 'Female']),
            start_date=fake.date_time_this_decade(),
            email=fake.email(),
            employee_no=fake.random_number(digits=6),
            salary_type=fake.word(),
            salary_amount=fake.random_number(digits=5),
            job_title=fake.job(),
            role=fake.random_element(elements=('Supervisor', 'Manager')),
            factory=factory
        )
        try:
            session.add(manager)
            session.commit()
        except IntegrityError:  # Catching unique constraint violation
            session.rollback()  # Rollback the transaction
            continue  # Continue with the next iteration

def create_fake_employees(num_employees=1000):
    factories = session.query(Factory).all()
    for _ in range(num_employees):
        factory = random.choice(factories)
        employee = Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=random.choice(['Male', 'Female']),
            start_date=fake.date_time_this_decade(),
            email=fake.email(),
            employee_no=fake.random_number(digits=6),
            salary_type=fake.word(),
            salary_amount=fake.random_number(digits=5),
            job_title=fake.job(),
            role=fake.random_element(elements=('Worker', 'Technician')),
            factory=factory
        )
        try:
            session.add(employee)
            session.commit()
        except IntegrityError:  # Catching unique constraint violation
            session.rollback()  # Rollback the transaction
            continue  # Continue with the next iteration

def create_fake_shifts(num_shifts=1000):
    factories = session.query(Factory).all()
    for _ in range(num_shifts):
        factory = random.choice(factories)
        shift = Shift(
            shift_name=fake.random_element(elements=('Morning', 'Afternoon', 'Night')),
            shift_supervisor=fake.name(),
            factory=factory
        )
        session.add(shift)
    session.commit()

if __name__ == "__main__":
    create_fake_factories()
    create_fake_managers()
    create_fake_employees()
    create_fake_shifts()
