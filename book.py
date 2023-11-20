import unicodedata

mystery = '\U0001f4a9'
print(mystery, 
      unicodedata.name(mystery), 
      unicodedata.lookup(unicodedata.name(mystery))
)

pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

pop_string = pop_bytes.decode('utf-8')
print(pop_string, pop_string == mystery)

mammoth = '''We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''


import re

print(*re.findall(r'\bc\w*\b', mammoth))
print(*re.findall(r'\bc\w{3}\b', mammoth))
print(*re.findall(r'\b\w*r\b', mammoth))
print(*re.findall(r'\b\w*[aioeyu]{3}\w*\b', mammoth))


import binascii

gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9' + 
                         '0401000000002c000000000100010000020144003b')
print(gif)

print(str(gif)[2:].startswith('GIF89a'))
print(int(binascii.hexlify(gif[7:5:-1]), 2), int(binascii.hexlify(gif[9:7:-1]), 2))

import struct

print(struct.unpack('<HH', gif[6:10]))

##################################################################################################################################################################################################
import csv

with open('books.csv') as f:
    data = csv.DictReader(f)
    #for i in data:
    #    print(i['book'])

with open('books.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=' ', quotechar="~")
    writer.writerow(['title', 'author', 'year'])
    import string
    for i, char in enumerate(zip(string.ascii_lowercase, string.ascii_uppercase), 1990):
        writer.writerow([char[0] + ' ' + char[1], char[1], round((i - i**0.5) * (-1)**i, 2)])


import sqlite3

connect = sqlite3.connect('book.db')
curs = connect.cursor()
curs.execute('''CREATE TABLE book (title VARCHAR(20), author VARCHAR(20), year FLOAT)''')

with open('books.csv') as f:
    reader = csv.reader(f, delimiter=' ', quotechar='~')
    next(reader)
    for item in reader:
        query = 'INSERT INTO book (title, author, year) VALUES(?,  ?,  ?)'
        curs.execute(query, item)

curs.execute("SELECT year FROM book")
print(*curs.fetchall(), sep='\n')


curs.execute("SELECT * FROM book ORDER BY year")
print(*curs.fetchall(), sep='\n')
print()

curs.execute("SELECT * FROM book ORDER BY year DESC")
print(*curs.fetchall(), sep='\n')
curs.close()
connect.close()

try:

    import sqlalchemy as sa

    conn = sa.create_engine('sqlite:///book.db')
    with conn.connect() as cursor:
        query = 'select title from book order by year desc'
        cursor.execute(query)
        cursor.commit()


except Exception as e:
    print(e)

finally:
    import os
    os.remove('book.db')