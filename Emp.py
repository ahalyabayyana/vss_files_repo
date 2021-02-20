class Employee:
    emp_code=20
    def __init__(self,ename,eage,esal):
        self.ename=ename
        self.eage=eage
        self.esal=esal
    def display(self):
        print("Emp name:",self.ename,"Emp age:",self.eage,"Emp Sal:",self.esal)    