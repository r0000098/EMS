import mysql.connector
import pandas as pd  


connection = mysql.connector.connect(
    user='root',
    password='12345', 
    host='localhost',
    database='N_EMS_db'  
)

cursor = connection.cursor()

def add_employee():
    cursor.execute("""
        INSERT INTO Employees_db (Name, Department, Salary, JoinDate)
        VALUES ('John Doe', 'Engineering', 75000.00, '2023-02-20')
    """)
    connection.commit()
    print("Employee added successfully!")


def view_employees():
    cursor.execute('SELECT * FROM Employees_db')
    employees = cursor.fetchall()
    print("\nEmployee Data:")
    employee_data = pd.DataFrame(employees, columns=[desc[0] for desc in cursor.description])
    print(employee_data)


def update_employee_salary():
    emp_id = int(input("Enter EmployeeID to update salary: "))
    new_salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE Employees_db SET Salary = %s WHERE EmployeeID = %s", (new_salary, emp_id))
    connection.commit()
    print("Employee salary updated!")


def delete_employee():
    emp_id = int(input("Enter EmployeeID to delete: "))
    cursor.execute("DELETE FROM Employees_db WHERE EmployeeID = %s", (emp_id,))
    connection.commit()
    print("Employee deleted successfully!")


def menu():
    while True:
        print("\n1. Add New Employee")
        print("2. View Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee_salary()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


menu()


cursor.close()
connection.close()
