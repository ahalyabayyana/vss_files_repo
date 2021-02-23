class Employee:
    __Ecode=401
    def __init__(self,ename,esal):
        self.__ename=ename
        self.__esal=esal
        self.__newsal=[]
    def show_emp(self):
        print(f"Employee name is {self.__ename} and Employee salary is {self.__esal}")
        print(f"New updated salary is {self.__newsal}")
    def set_ename(self,name):
        self.__ename=name
    def set_esal(self,sal):
        self.__esal=sal
    def update_ecode(self,newcode):
        Employee.__Ecode=newcode
        print("New Employee code is ",Employee.__Ecode )
    def list_of_sal(self,newsal):
        self.__newsal.append(newsal)
    def set_ename_esal(self,name,sal):
        self.set_ename(name)
        self.set_esal(sal)
    def upper_ename(self):
        self.__ename=str.upper(self.__ename)
    def append_ename(self):
        self.__ename=self.__ename.replace(self.__ename,self.__ename+" Hello")
    def upper_append(self):
        self.upper_ename()
        self.append_ename()

        





e1=Employee("Rekha",2000)    
# # e1.show_emp()
# print("Dict variable for Class Employee is :",Employee.__dict__) 
# print("Dict variable for object of  Employee e1 is :",e1.__dict__) 
# e1.__ename="Ahalya"
# e1.show_emp()
# print("Dict variable for object of  Employee e1 is :",e1.__dict__) 
# e1.set_esal(1500)
# e1.list_of_sal(3000)

# # e1.__newsal.append(4000)
e1.set_ename_esal("Ahalya Rao",5000)
e1.upper_append()
e1.show_emp()