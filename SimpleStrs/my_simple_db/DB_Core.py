import shelve


class DataBase:

    def __init__(self, name):
        self.name = name
        self.data = shelve.open(filename=name)

    def __del__(self):
        # print('db saved and closed')
        self.data.close()

    def __repr__(self):
        return self.name

    def read(self):
        return self.data

    def update(self, name, value):
        self.data[name] = value

    def delete(self, name):
        if self.data.get(name):
            self.data.pop(name)
        else:
            print('error: Data not exists')


if __name__ == '__main__':
    db = DataBase('my_db')
    print('test start DB_Core.py')
    db.update('alex', {'payment': '20000', 'work': 'management'})
    db.update('lois', {'payment': '15000', 'work': 'programmer'})
    my_db = db.read()
    for elem in my_db.items():
        if elem['alex']:
            print(elem['alex']['payment'])
