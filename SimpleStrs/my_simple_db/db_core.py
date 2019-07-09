import shelve


db = shelve.open('db.core')


class DBObject:
    def __init__(self):
        pass

    def __str__(self):
        pass


class DBCore:

    def __init__(self, name):
        self.name = name
        self.data = shelve.open(filename=name)

    def __del__(self):
        self.data.close()


if __name__ ==  '__main__':
    db = DBCore('my_db')
    print('test start db_core.py')