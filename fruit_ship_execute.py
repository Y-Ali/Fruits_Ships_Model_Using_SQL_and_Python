from db_connection import *
from ship import Ship
from fruit import Fruit




fruit_obj = Fruit() # this one is to get all the fruits in the table

fruit_obj.save_fruit("bananas",90.7,"good",'2019-06-19')
fruit_obj.get_all_fruits()





# add and save fruits using save_fruit() method, to fruits table in database
# fruit = Fruit()
# fruit.add_save_fruit("apple",10.5,"good",'2019-11-15')
# fruit.add_save_fruit("pear",4.5,"very good",'2019-01-21')
# fruit.add_save_fruit("banana",9.5,"perfect",'2019-07-30')



# ship = Ship()
# ship.add_cargo(fruit.type_of_fruit)
# print(ship.cargo_list)

# fruit1 = Fruit("banana", 10)
# fruit2 = Fruit("apple", 100)
# fruit3 = Fruit("pear", 23)
# fruit4 = Fruit("pineapple", 34)

# boat.add_cargo(fruit1)
# boat.add_cargo(fruit2)
# boat.add_cargo(fruit3)
# boat.add_cargo(fruit4)

# boat.list_cargo_items()




