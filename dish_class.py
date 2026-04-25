class Cooking:
    def __init__(self, vegetables):
        self.vegetables = vegetables
    def wash(self):
        for i in self.vegetables:
            is_clean = True
            while is_clean:
                check = input(f'Is {i} it clean enter yes/no:')
                if check == 'yes':
                    print(f'{i} is clean')
                    is_clean = Fals
                else:
                    print(f'Wash {i} again!')
        print("All Vegetables are clean")
        return self.vegetables
    def cut(self):
        for i in self.vegetables:
            while True:
                cut = input(f'Is {i} it cut enter yes/no:')
                if cut == 'yes':
                    print(f'{i} is cut')
                else:
                    print(f'Please wait until you finish cutting {j}.')
                    print(f"Cut{j}") 
Dish = Cooking(vegetables=["Carrot", "Green chilli", "curry leaves", "onion"])
Dish.wash()

