class Animal:
    Type="Animal"
    list_animals=[]
    def __init__(self,name,color,breed):
        self.name=name
        self.color=color
        self.breed=breed
    def show_animal(self):
        print("Name of animal is :",self.name,", Color of animal is ",self.color," and Breed of animal is :",self.breed)   
        print("list of no of animlas is :",self.list_animals)
a=Animal("Dog","Brown","German Shephard")
a.show_animal() 
a.list_animals.append("Dog")
Animal.list_animals.append("cat") 
print(Animal.list_animals)
print(a.list_animals)