from db_connection import *
class Fruit:

    def __init__(self, name = '' , kg = '', quality = '', exp_date = ''):
        self.type_of_fruit = name
        self.kg_of_fruit = kg
        self.quality = quality
        self.expiration_date = exp_date

        #self.cursor = self.ships_fruits_db.cursor()

    def save_fruit(self,type_of_fruit,kg_of_fruit,quality,expiration_date):
        try:
            query = (f"INSERT INTO Fruits (fruit_name, fruit_kg, fruit_quality, fruit_expiration_date)"
                     f"VALUES ('{type_of_fruit}', {kg_of_fruit} ,'{quality}', '{expiration_date}')")
            #print(query)
            cursor.execute(query)
            ships_fruits_db.commit()

            print("\nTable updated, 1 row affected.")

        except Exception as ermsg:
            print ("\nPânico !! ! !!")
            print(ermsg)
            raise

    def get_all_fruits(self):
        try:
            fruits = cursor.execute("SELECT * FROM Fruits")
            column = cursor.description

            #row = fruits.fetchall() # refactor to while, fetchone()
            for fruit_item in fruits:
                print(column[0][0], ":", fruit_item.fruit_name)
                Fruit(fruit_item.fruit_name, fruit_item.fruit_kg, fruit_item.fruit_quality,fruit_item.fruit_expiration_date)  # Creates a fruit object.
                # print(Fruit(fruit_item.fruit_name, fruit_item.fruit_kg, fruit_item.fruit_quality, fruit_item.fruit_expiration_date))

            print("\nOperation has been completed.")

        except Exception as ermsg:
            print("\nPânico !! ! !! The data has not been read. Please refer to error message.")
            print(ermsg)
            raise
