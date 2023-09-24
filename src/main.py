import os
import sqlite3
from openpyxl import load_workbook

db_filename = '../build/aircrafts.db'
schema_filename = '../src/aircrafts_schema.sql'

if os.path.exists(db_filename):
    os.remove(db_filename)


def get_families(conn):
    cursor = conn.cursor()
    cursor.execute("""
                select * from family
                """)
    families = dict()
    for row in cursor.fetchall():
        families[row[1]] = row[0]
    return families


is_exist = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if is_exist:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        wb = load_workbook(filename='../test/aircrafts_data.xlsx')
        ws = wb["AIRCRAFTS"]

        conn.execute("insert into family (name) values ('fam1'),('fam2'),('fam3')")
        families = get_families(conn)


    else:
        print('Database exists, assume schema does, too.')

