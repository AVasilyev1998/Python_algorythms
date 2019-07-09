import shelve


db = shelve.open('db.txt')
print(db['db'])
db.close()