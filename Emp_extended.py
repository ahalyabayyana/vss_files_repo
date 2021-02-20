import Emp
import pickle
e1=Emp.Employee("Rekha",35,2500)
# e1.display()
with open("emp1.dat","wb") as f:
    pickle.dump(e1,f)

with open("emp1.dat","rb") as f:
    obj1=pickle.load(f) 
obj1.display()   