"""
"""
import re
from mimesis import Person
from mimesis import Address
import shelve


AMOUNT = 2000


class MyPerson:
    def __init__(self, full_name, phone, federal_subject, address):
        self.name = full_name
        self.phone = phone
        self.federal_object = federal_subject
        self.address = address

    def __repr__(self):
        return ' | '.join([self.name, self.phone, self.address, self.federal_object])


person_dict = {}
for i in range(1, AMOUNT + 1):
    rus = Person('ru')
    rus_adr = Address('ru')
    tmp_person = MyPerson(rus.full_name(), rus.telephone(), rus_adr.federal_subject(), rus_adr.address())
    person_dict[i] = tmp_person


for k, v in person_dict.items():
    print(f'{k} | {v}')


db = shelve.open('db.txt')
db['db'] = person_dict
db.close()


