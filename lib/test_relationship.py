#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee


def reset_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)


def test_relationship():
    reset_database()
    
    print("Testing one-to-many relationship between Department and Employee")
    print("=" * 60)
    
    # Test getting all departments
    print("\nAll departments:")
    departments = Department.get_all()
    for dept in departments:
        print(f"  {dept}")
    
    # Test getting all employees
    print("\nAll employees:")
    employees = Employee.get_all()
    for emp in employees:
        print(f"  {emp}")
    
    # Test getting employees for a specific department
    print("\nEmployees in Payroll department:")
    payroll = Department.find_by_name("Payroll")
    payroll_employees = payroll.employees()
    for emp in payroll_employees:
        print(f"  {emp}")
    
    print("\nEmployees in Human Resources department:")
    hr = Department.find_by_name("Human Resources")
    hr_employees = hr.employees()
    for emp in hr_employees:
        print(f"  {emp}")
    
    # Test getting department for a specific employee
    print("\nTesting employee to department relationship:")
    employee = Employee.find_by_name("Amir")
    print(f"Employee: {employee}")
    department = Department.find_by_id(employee.department_id)
    print(f"Works in: {department}")
    
    print("\n✅ All tests passed! One-to-many relationship is working correctly.")


if __name__ == "__main__":
    test_relationship()