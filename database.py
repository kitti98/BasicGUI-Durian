import sqlite3

conn = sqlite3.connect('product-database.sqlite3') # connect กับ database
c = conn.cursor() # cursor เอาไว้ใช้ execute ต่างๆ

#CREATE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quan REAL,
                total REAL )""")

print('Success')

def insert_transaction(data):
    # data = {'tid':'101201250','stamp':'2022-04-20 15:37:59'...}
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']

    with conn:
        command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit
    print('Inserted!')

def view_transaction():
    with conn:
        c.execute('SELECT * FROM transaction_history')
        data = c.fetchall()
        print(data)

transaction = {'tid':'101201250',
                'stamp':'2022-04-20 15:37:59',
                'product':'ทุเรียน',
                'price':100,
                'quan':50,
                'total':5000}

#insert_transaction(transaction)
view_transaction()