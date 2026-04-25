class House:
    def __init__(self,color,rooms):
       self.color = color
       self.rooms = rooms
    def modify(self):
        print("Selected Color", self.color)
        print("Number of rooms in the house", self.rooms)
    def display(self):
        final_result = "The Color Selected is" + self.color
        return final_result
House1 = House("Green", 4)
House1.modify()
a = (House1.display())
print(House1.display())
House2 = House("Red", 5)


