import employee_info as main

def test_get_employee_by_age_range():
    result=[]
    expected_result=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = main.get_employees_by_age_range(20,30)

    assert result == expected_result

def test_get_employees_by_dept():
    result=[]
    expected_result = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result = main.get_employees_by_dept("Engineering")

    assert result == expected_result

def test_calc_average_salary():
    
    expected_result = (50000+60000+56000+70000+65000+60000)/6
    result = main.calculate_average_salary()

    assert result == expected_result