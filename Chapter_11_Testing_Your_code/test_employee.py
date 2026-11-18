#11-3 Employee
from employe_class import Employee
import pytest

# def test_give_fixed_raise():
#     """test unit which adds fixed raise"""
#     class1 = Employee('Anton','Fomin', 1000)
#     class1.give_raise(5000)
#     assert class1.salary == 6000

# def test_give_fixed_raise1():
#     """test unit which adds fixed raise"""
#     class2 = Employee('Anton','Fomin', 1000)
#     class2.give_raise(2000)
#     assert class2.salary == 3000

@pytest.fixture
def employee_class_instances():
    """function that should store all the employee instances""" 
    employee_class_instances = Employee('Anton','Fomin', 1000)
    return employee_class_instances

def test_give_fixed_raise(employee_class_instances):
    """test unit which adds fixed raise"""
    employee_class_instances.give_raise(5000)
    assert employee_class_instances.salary == 6000

def test_give_fixed_raise1(employee_class_instances):
    """test unit which adds fixed raise"""
    employee_class_instances.give_raise(2000)
    assert  employee_class_instances.salary == 3000