from sql_alchemy.db_management import DbManagement
from sql_alchemy.models import Projektas

# add_value
# delete_value
# update value
# filter value
# get value

class Game(DbManagement):

    def insert_data_in_db(self):

        name = input('Ivesk prekes pavadinima: ')
        price = input('Ivesk prekes kaina: ')
        location = input ('Ivesk prekes buvimo vieta: ')
        project = Projektas(name=name,price =price,location=location)
        self.add_value(project)

    def filter_by_name_(self):
        name = input('Iveskit prekes pavadinima: ')
        # result = self.filter_by_name(name=name)
        print(name)

    def delete_value_(self):
        value = input('Ivesk prekes id: ')
        self.delete_value(int(value))

    def update_value_(self):
        value = input('Ivesk prekes id: ')
        name = input('Ivesk prekes pavadinima: ')
        self.update_value(value, name)

    def get_value_(self):
        value = input('Ivesk prekes id: ')

        print(self.get_value_by_id(value))

    def run(self):
        while True:
            value = int(input('Paduok skaiciu: '))
            if value == 6:
                break
            data = {
                1: self.insert_data_in_db,
                2: self.filter_by_name_,
                3: self.delete_value_,
                4: self.update_value_,
                5: self.get_value_
            }
            data[value]()

