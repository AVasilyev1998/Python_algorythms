import shelve
from my_simple_db.DB_Core import DataBase


class DBDriver:

    def __init__(self):
        self.active_db = shelve.open('active_dbs')
        self.stopped_db = shelve.open('stopped_dbs')

    def create_db(self, name):
        tmpDb = DataBase(name)
        self.stopped_db[name] = tmpDb

    def start_db(self, name):
        if self.stopped_db.get(name):
            self.active_db[name] = self.stopped_db.get(name)
            self.stopped_db.pop(name)
        else:
            print('error: Start DB error')

    def createstart_db(self, name):
        self.create_db(name)
        self.start_db(name)

    def stop_db(self, name):
        if self.active_db.get(name):
            self.stopped_db[name] = self.active_db.get(name)
            self.active_db.pop(name)

    def show_active(self):
        if self.active_db.__len__() == 0:
            print('there are no active db`s')
        else:
            print('active db`s: ', end='')
            for i in self.active_db.keys():
                print(i, end=' ')
            print()

    def __del__(self):
        self.active_db.close()
        self.stopped_db.close()


if __name__ == '__main__':
    print('BD_Driver test start from DB_Driver.py')
    driver = DBDriver()
    # driver.show_active()
    driver.create_db('somedb')
    # driver.createstart_db('my_db2')
    # driver.show_active()
