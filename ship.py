class Ship:

    def __init__(self, name, location = '', destination = ''):
        self.name = name
        self.current_location = location
        self.destination = destination
        self.cargo_list = []


    def sail(self):
        print("Sailing from ", self.current_location,"to", self.destination)

    def add_cargo(self,cargo):
        self.cargo_list.append(cargo)

    def list_cargo_items(self):
        for item in self.cargo_list:
            print(item.type_of_fruit,": Carrying", item.kg_of_fruit,"kg")

    def remove_fruit(self):
        print("delete, delete, delete, delete")







