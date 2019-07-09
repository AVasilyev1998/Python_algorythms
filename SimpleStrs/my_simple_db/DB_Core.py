import shelve


class DBCore:

    def __init__(self, name):
        self.name = name
        self.data = shelve.open(filename=name)

    def __del__(self):
        print('db saved and closed')
        self.data.close()

    def __repr__(self):
        return self.name




if __name__ == '__main__':
    db = DBCore('my_db')
    print('test start DB_Core.py')