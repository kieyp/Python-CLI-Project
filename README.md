# Python-CLI-Project


Factory Management System

The Factory Management System is a command-line application that allows users to manage factories, managers, employees, and shifts within those factories. It provides functionality to add, list, and manipulate data related to factories and their personnel.



Features

-Add factories with location and type information.
-Add managers and employees to specific factories, with details such as name, gender, email, employee number, salary, job title, and role.
-Add shifts to factories, specifying the shift name and supervisor.
List all factories, managers, employees, and shifts associated with a factory.
-Retrieve detailed information about managers, employees, and shifts.



Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your_username/factory_management_system.git
Navigate to the project directory:

bash
Copy code
cd factory_management_system
Install the required dependencies:


Copy code
pip install -r requirements.txt
Ensure you have a SQLite database named factory_data.db in the project directory. You can create the database using the provided schema and populate it with sample data if needed.


Run the main script to start the Factory Management System:

Copy code
python commands.py
Usage
Upon running the script, you'll be presented with a menu where you can choose from various options to manage factories and their personnel:

Add Factory
Add Manager
Add Employee
Add Shift
List Factories
List Managers
List Employees
List Shifts
Exit
Follow the prompts to perform the desired operations.

Contributors
Boniface cheruiyot
License
This project is licensed under the MIT License - see the LICENSE file for details.