import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Factory, Manager, Employee, Shift, Base

# Create engine and bind to existing database
engine = create_engine('sqlite:///factory_data.db')
Base.metadata.bind = engine

# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_factory(args):
    location = input("Enter factory location: ")
    type = input("Enter factory type: ")

    new_factory = Factory(location=location, type=type)
    session.add(new_factory)
    session.commit()
    print("Factory added successfully.")

def add_manager(args):
    factory_id = input("Enter factory ID: ")
    first_name = input("Enter manager's first name: ")
    last_name = input("Enter manager's last name: ")
    gender = input("Enter manager's gender: ")
    email = input("Enter manager's email: ")
    employee_no = input("Enter manager's employee number: ")
    salary_type = input("Enter manager's salary type: ")
    salary_amount = int(input("Enter manager's salary amount: "))
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

def add_employee(args):
    factory_id = input("Enter factory ID: ")
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    gender = input("Enter employee's gender: ")
    email = input("Enter employee's email: ")
    employee_no = input("Enter employee's employee number: ")
    salary_type = input("Enter employee's salary type: ")
    salary_amount = int(input("Enter employee's salary amount: "))
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

def add_shift(args):
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

def delete_entity(args):
    entity_type = input("Enter entity type to delete (employee, manager, shift): ")
    if entity_type == "employee":
        delete_employee()
    elif entity_type == "manager":
        delete_manager()
    elif entity_type == "shift":
        delete_shift()
    else:
        print("Invalid entity type.")

def delete_employee():
    factory_id = input("Enter factory ID: ")
    employee_id = input("Enter employee ID to delete: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        employee = session.query(Employee).filter_by(id=employee_id, factory_id=factory_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            print("Employee deleted successfully.")
        else:
            print("Employee not found in the specified factory.")
    else:
        print("Factory not found.")

def delete_manager():
    factory_id = input("Enter factory ID: ")
    manager_id = input("Enter manager ID to delete: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        manager = session.query(Manager).filter_by(id=manager_id, factory_id=factory_id).first()
        if manager:
            session.delete(manager)
            session.commit()
            print("Manager deleted successfully.")
        else:
            print("Manager not found in the specified factory.")
    else:
        print("Factory not found.")

def delete_shift():
    factory_id = input("Enter factory ID: ")
    shift_id = input("Enter shift ID to delete: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        shift = session.query(Shift).filter_by(id=shift_id, factory_id=factory_id).first()
        if shift:
            session.delete(shift)
            session.commit()
            print("Shift deleted successfully.")
        else:
            print("Shift not found in the specified factory.")
    else:
        print("Factory not found.")

def update_entity(args):
    entity_type = input("Enter entity type to update (employee, manager, shift): ")
    if entity_type == "employee":
        update_employee()
    elif entity_type == "manager":
        update_manager()
    elif entity_type == "shift":
        update_shift()
    else:
        print("Invalid entity type.")

def update_employee():
    factory_id = input("Enter factory ID: ")
    employee_id = input("Enter employee ID to update: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        employee = session.query(Employee).filter_by(id=employee_id, factory_id=factory_id).first()
        if employee:
            # Update employee attributes
            employee.first_name = input("Enter employee's first name: ")
            employee.last_name = input("Enter employee's last name: ")
            employee.gender = input("Enter employee's gender: ")
            employee.email = input("Enter employee's email: ")
            employee.employee_no = input("Enter employee's employee number: ")
            employee.salary_type = input("Enter employee's salary type: ")
            employee.salary_amount = int(input("Enter employee's salary amount: "))
            employee.job_title = input("Enter employee's job title: ")
            employee.role = input("Enter employee's role: ")
            session.commit()
            print("Employee updated successfully.")
        else:
            print("Employee not found in the specified factory.")
    else:
        print("Factory not found.")

def update_manager():
    factory_id = input("Enter factory ID: ")
    manager_id = input("Enter manager ID to update: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        manager = session.query(Manager).filter_by(id=manager_id, factory_id=factory_id).first()
        if manager:
            # Update manager attributes
            manager.first_name = input("Enter manager's first name: ")
            manager.last_name = input("Enter manager's last name: ")
            manager.gender = input("Enter manager's gender: ")
            manager.email = input("Enter manager's email: ")
            manager.employee_no = input("Enter manager's employee number: ")
            manager.salary_type = input("Enter manager's salary type: ")
            manager.salary_amount = int(input("Enter manager's salary amount: "))
            manager.job_title = input("Enter manager's job title: ")
            manager.role = input("Enter manager's role: ")
            session.commit()
            print("Manager updated successfully.")
        else:
            print("Manager not found in the specified factory.")
    else:
        print("Factory not found.")

def update_shift():
    factory_id = input("Enter factory ID: ")
    shift_id = input("Enter shift ID to update: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        shift = session.query(Shift).filter_by(id=shift_id, factory_id=factory_id).first()
        if shift:
            # Update shift attributes
            shift.shift_name = input("Enter shift name: ")
            shift.shift_supervisor = input("Enter shift supervisor: ")
            session.commit()
            print("Shift updated successfully.")
        else:
            print("Shift not found in the specified factory.")
    else:
        print("Factory not found.")

def list_factories(args):
    factories = session.query(Factory).all()
    factory_data = []
    for factory in factories:
        factory_data.append({
            "id": factory.id,
            "location": factory.location,
            "type": factory.type
        })
    return factory_data

def list_managers(args):
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        manager_data = []
        for manager in factory.managers:
            manager_data.append({
                "id": manager.id,
                "first_name": manager.first_name,
                "last_name": manager.last_name,
                "gender": manager.gender,
                "start_date": manager.start_date,
                "email": manager.email,
                "employee_no": manager.employee_no,
                "salary_type": manager.salary_type,
                "salary_amount": manager.salary_amount,
                "job_title": manager.job_title,
                "role": manager.role
            })
        return manager_data
    else:
        return "Factory not found."

def list_employees(args):
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        employee_data = []
        for employee in factory.employees:
            employee_data.append({
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "gender": employee.gender,
                "start_date": employee.start_date,
                "email": employee.email,
                "employee_no": employee.employee_no,
                "salary_type": employee.salary_type,
                "salary_amount": employee.salary_amount,
                "job_title": employee.job_title,
                "role": employee.role
            })
        return employee_data
    else:
        return "Factory not found."

def list_shifts(args):
    factory_id = input("Enter factory ID: ")
    factory = session.query(Factory).filter_by(id=factory_id).first()
    if factory:
        shift_data = []
        for shift in factory.shifts:
            shift_data.append({
                "id": shift.id,
                "shift_name": shift.shift_name,
                "shift_supervisor": shift.shift_supervisor
            })
        return shift_data
    else:
        return "Factory not found."

def main():
    parser = argparse.ArgumentParser(description="Factory Management System")

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Subcommands for adding entities
    add_factory_parser = subparsers.add_parser("add_factory", help="Add a factory")
    add_factory_parser.set_defaults(func=add_factory)

    add_manager_parser = subparsers.add_parser("add_manager", help="Add a manager")
    add_manager_parser.set_defaults(func=add_manager)

    add_employee_parser = subparsers.add_parser("add_employee", help="Add an employee")
    add_employee_parser.set_defaults(func=add_employee)

    add_shift_parser = subparsers.add_parser("add_shift", help="Add a shift")
    add_shift_parser.set_defaults(func=add_shift)

    # Subcommands for deleting entities
    delete_entity_parser = subparsers.add_parser("delete_entity", help="Delete an entity")
    delete_entity_parser.set_defaults(func=delete_entity)

    # Subcommands for updating entities
    update_entity_parser = subparsers.add_parser("update_entity", help="Update an entity")
    update_entity_parser.set_defaults(func=update_entity)

    # Subcommands for listing entities
    list_factories_parser = subparsers.add_parser("list_factories", help="List all factories")
    list_factories_parser.set_defaults(func=list_factories)

    list_managers_parser = subparsers.add_parser("list_managers", help="List all managers")
    list_managers_parser.set_defaults(func=list_managers)

    list_employees_parser = subparsers.add_parser("list_employees", help="List all employees")
    list_employees_parser.set_defaults(func=list_employees)

    list_shifts_parser = subparsers.add_parser("list_shifts", help="List all shifts")
    list_shifts_parser.set_defaults(func=list_shifts)

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
        print("9. Delete Entity")
        print("10. Update Entity")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_factory(None)
        elif choice == "2":
            add_manager(None)
        elif choice == "3":
            add_employee(None)
        elif choice == "4":
            add_shift(None)
        elif choice == "5":
            factories = list_factories(None)
            for factory in factories:
                print(factory)
            input("Press Enter to continue...")
        elif choice == "6":
            managers = list_managers(None)
            for manager in managers:
                print(manager)
            input("Press Enter to continue...")
        elif choice == "7":
            employees = list_employees(None)
            for employee in employees:
                print(employee)
            input("Press Enter to continue...")
        elif choice == "8":
            shifts = list_shifts(None)
            for shift in shifts:
                print(shift)
            input("Press Enter to continue...")
        elif choice == "9":
            delete_entity(None)
        elif choice == "10":
            update_entity(None)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
