from my_simple_db.db_core import DBCore


class BDDriver:

    active_db = {}
    stopped_db = {}

    def __init__(self):
        pass

    @classmethod
    def create_db(cls, name):
        cls.stopped_db[name] = DBCore(name=name)

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
            for i in cls.active_db.keys():
                print(i)


if __name__ == '__main__':
    print('BD_Driver test start from BD_Driver.py')
    driver = BDDriver()
    driver.show_active()
    driver.createstart_db('my_db')
    driver.show_active()
