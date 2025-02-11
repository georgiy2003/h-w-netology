from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == "__main__":
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    employees = get_employees()
    print("Список сотрудников:", employees)
    total_salary = calculate_salary(employees)
    print(f"Общая зарплата: {total_salary}")















