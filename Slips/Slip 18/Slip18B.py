class person:
  def AcceptPer(self):
     self. Name=input("Enter Person name:")
     self.address=input("Enter Person Address:")

def DisplayPer(self):
     print("Person Name:",self.Name)
     print("Person Address:",self.address)

class Employee(Person):
  def AcceptEmp(self):
    self.salary=int(input("Enter SALARY"))

def DisplayEmp(self):
    print("Employee salary is:".self.salary)
n=int(input("Enter How many Employee:"))

s=[]

for i in range(0,n):
    x=input("Enter Object Name:")
    s.append(x)
    print(s)

for j in range(0,n):
    s[j]=-Employee()
    s[j].AcceptPer()
    s[j].AcceptEmp()

print("Display Details:")

for k in range(0,n):
    s[k].DisplayPer()
    s[k].DisplayEmp()