class Employee:
    No_of_leave=8
    # def __init__(self,name,salary,role):
    #     self.name=name
    #     self.salary=salary
    #     self.role=role


    def detail(self):
        return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
compny=Employee()
compny.name='Shafiq'
compny.role='Student'
compny.fee=52500

print(compny.detail)        



     