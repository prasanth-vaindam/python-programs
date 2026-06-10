class Car:
   def  __init__(self,name,color,model,year,milage=15):
       self.name=name
       self.color=color
       self.model=model
       self.year=year
       self.milage=milage
   def display(self):
       print(f"{self.name}'s favourite car is {self.model} which is manufactured in year {self.year} of color {self.color}")
   def milage_car(self):
       print(f"The milage of {self.name}'s car is {self.milage}")


abhilash = Car("abhi","olive green","range rover",2020)
abhilash.display()
abhilash.milage_car()
mani = Car("teja","black","G-wagon",2020)
mani.display()
mani.milage_car()
raju = Car("chimtu","white","thar",2020)
raju.display()
raju.milage_car()