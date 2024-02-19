from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Factory, Manager, Employee, Shift, Base

# Create engine and bind to existing database
engine = create_engine('sqlite:///factory_data.db')
Base.metadata.bind = engine

# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_factory():
    location = input("Enter factory location: ")
    type = input("Enter factory type: ")

    new_factory = Factory(location=location, type=type)
    session.add(new_factory)
    session.commit()
    print("Factory added successfully.")

def add_manager():
    factory_id = input("Enter factory ID: ")
    first_name = input("Enter manager's first name: ")
    last_name = input("Enter manager's last name: ")
    gender = input("Enter manager's gender: ")
    email = input("Enter manager's email: ")
    employee_no = input("Enter manager's employee number: ")
    salary_type = input("Enter manager's salary type: ")
    
    while True:
        try:
            salary_amount = int(input("Enter manager's salary amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the salary amount.")

    job_title = input("Enter manager's job title: ")
    role = input("Enter manager's role: ")

    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        new_manager = factory.add_manager(
            first_name, last_name, gender, email,
            employee_no, salary_type, salary_amount,
            job_title, role
        )
        session.add(new_manager)
        session.commit()
        print("Manager added successfully.")
    else:
        print("Factory not found.")

def add_employee():
    factory_id = input("Enter factory ID: ")
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    gender = input("Enter employee's gender: ")
    email = input("Enter employee's email: ")
    employee_no = input("Enter employee's employee number: ")
    salary_type = input("Enter employee's salary type: ")
    while True:
        try:
            salary_amount = int(input("Enter employee's salary amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the salary amount.")

    job_title = input("Enter employee's job title: ")
    role = input("Enter employee's role: ")

    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        new_employee = factory.add_employee(
            first_name, last_name, gender, email,
            employee_no, salary_type, salary_amount,
            job_title, role
        )
        session.add(new_employee)
        session.commit()
        print("Employee added successfully.")
    else:
        print("Factory not found.")

def add_shift():
    factory_id = input("Enter factory ID: ")
    shift_name = input("Enter shift name: ")
    shift_supervisor = input("Enter shift supervisor: ")

    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        new_shift = factory.add_shift(shift_name, shift_supervisor)
        session.add(new_shift)
        session.commit()
        print("Shift added successfully.")
    else:
        print("Factory not found.")

def list_factories():
    factories = session.query(Factory).all()
    for factory in factories:
        factory_data = {key: value for key, value in factory.__dict__.items() if not key.startswith('_')}
        print(factory_data)

def list_managers():
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        managers = factory.list_managers()
        for manager in managers:
            manager_data = {key: value for key, value in manager.__dict__.items() if not key.startswith('_')}
            print(manager_data)
    else:
        print("Factory not found.")

def list_employees():
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        employees = factory.list_employees()
        for employee in employees:
            employee_data = {key: value for key, value in employee.__dict__.items() if not key.startswith('_')}
            print(employee_data)
    else:
        print("Factory not found.")

def list_shifts():
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        shifts = factory.list_shifts()
        for shift in shifts:
            shift_data = {key: value for key, value in shift.__dict__.items() if not key.startswith('_')}
            print(shift_data)
    else:
        print("Factory not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Factory")
        print("2. Add Manager")
        print("3. Add Employee")
        print("4. Add Shift")
        print("5. List Factories")
        print("6. List Managers")
        print("7. List Employees")
        print("8. List Shifts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_factory()
        elif choice == "2":
            add_manager()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            add_shift()
        elif choice == "5":
            list_factories()
        elif choice == "6":
            list_managers()
        elif choice == "7":
            list_employees()
        elif choice == "8":
            list_shifts()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
