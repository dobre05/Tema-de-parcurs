
class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary


    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager (Employee):
    mgr_count = 0

    def __init__ (self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks= tasks
        self.department = "IETTI" + department
        Manager.mgr_count +=1
        

    def display_employee(self):
        r=X%4

        if r==0:
            print( "Salary:", self.salary)

        elif r==1:
            print ("Name:", self.name)

        elif r==2:
            print ("Department:", self.department)

        elif r==3:
            print ("Tasks:", list(self.tasks.keys()))

    
X=13
Y=5

task_names = ["Sedinta", "Documentatie"]

managers = []
for i in range(Y // 3):
    mgr= Manager(
        name=f"Manager{i+1}",
        salary=5000 + i*500,
        tasks={task_names[i*2]: "New", task_names[i*2+1]: "In progress"},
        department="Software"
    )
    managers.append(mgr)

e1 = Employee("Andrei", 3000)
e2 = Employee("Mihai", 3500)

print("\n Managers ")
for m in managers:
    m.display_employee()

print("\n Employee ")
e1.display_employee()
e2.display_employee()

print("\nTotal Employee count:", Employee.empCount)
print("Total Manager count:", Manager.mgr_count)
    
