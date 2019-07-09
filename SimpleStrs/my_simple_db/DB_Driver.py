from my_simple_db.DB_Core import DataBase


class BDDriver:

    active_db = {}
    stopped_db = {}

    def __init__(self):
        pass

    @classmethod
    def create_db(cls, name):
        cls.stopped_db[name] = DataBase(name=name)

    @classmethod
    def start_db(cls, name):
        if cls.stopped_db.get(name):
            cls.active_db[name] = cls.stopped_db.get(name)
            cls.stopped_db.pop(name)
        else:
            print('error: Start DB error')

    @classmethod
    def createstart_db(cls, name):
        cls.create_db(name)
        cls.start_db(name)

    @classmethod
    def stop_db(cls, name):
        if cls.active_db.get(name):
            cls.stopped_db[name] = cls.active_db.get(name)
            cls.active_db.pop(name)

    @classmethod
    def show_active(cls):
        if cls.active_db.__len__() == 0:
            print('there are no active db`s')
        else:
            print('active db`s: ', end='')
            for i in cls.active_db.keys():
                print(i, end=' ')
            print()


if __name__ == '__main__':
    print('BD_Driver test start from DB_Driver.py')
    driver = BDDriver()
    driver.show_active()
    driver.createstart_db('my_db')
    driver.createstart_db('my_db2')
    driver.show_active()
