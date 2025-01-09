
class Employee:
    def __init__(self, emp_id, fname, lname, salary):
        self.emp_id = emp_id
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __str__(self):
        return f"Employee(ID: {self.emp_id}, Name: {self.fname} {self.lname}, Salary: {self.salary})"

    def __eq__(self, other):
        return (
            isinstance(other, Employee) and
            self.emp_id == other.emp_id and
            self.fname == other.fname and
            self.lname == other.lname and
            self.salary == other.salary
        )
    def __hash__(self):
        # return hash(str(self.emp_id) + self.fname + self.lname + str(self.salary))
        return hash( (self.emp_id, self.fname,  self.lname, self.salary) )

e1 = Employee(1, 'a', 'b', 3)
print(e1)
print(hash(e1))
print(hex(166277589369))
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
# 89 =  8 * 10 + 9 * 1
# FF = 16 * 16 + 16 * 1

# 0000026B6EAA9790
# 129867516281
# 1E3CB509790
#      26b6eaa9790
# 1C19D5F9700
# 1C19D5F9700