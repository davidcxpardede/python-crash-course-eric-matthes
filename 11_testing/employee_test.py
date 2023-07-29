import pytest
from employee import Employee

@pytest.fixture
def employee():
    """An employee who has their salary raised."""
    employee = Employee('david', 'pardede', 11000)
    return employee

def test_give_default_raise(employee):
    """Test the give_raise() method by default value."""
    employee.give_raise()
    assert employee.annual_salary == 16000
    
def test_give_custom_raise(employee):
    """Test the give_raise() method by custom value."""
    employee.give_raise(1000)
    assert employee.annual_salary == 12000