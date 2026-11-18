#11-3 Employee

class Employee:
    """Class that represents the first and last name of an employee and 
    their salary."""

    def __init__(self,first,last,salary):
        """Class Initialization"""
        self.first = first
        self.last = last
        self.salary = int(salary)

    # def salary(self, salary):
    #     """function which represents the salary"""
    #     self.salary = salary

    def give_raise(self, increase):
        """function which has to increase the defalut salary"""
        increase = int(increase)
        self.salary = self.salary + increase



        