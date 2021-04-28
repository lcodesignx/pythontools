#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('example.db')
conn.execute('''
        CREATE TABLE stocks (
            date text,
            trans text,
            symbol text,
            qty real,
            price real
        )''')
purchases = [('2020-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2020-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2020-04-06', 'SELL', 'IBM', 500, 53.00),
             ('2020-07-21', 'BUY', 'RHAT', 100, 35.14),]

c = conn.cursor()
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

conn.commit()
conn.close()
