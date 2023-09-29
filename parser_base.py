import json
import sqlite3
from datetime import date

current_date = date.today()

db = sqlite3.connect('db.sqlite3')
sql = db.cursor()

with open("json/2.json", 'r', encoding='utf-8-sig') as f:
    read = f.read()

data = json.loads(read)
base = {}

for i in data['data']:
    base['Склад'] = i['Склад']
    base['Номенклатура'] = i['Номенклатура']
    base['КонечныйОстаток'] = float(
        i['КонечныйОстаток'].replace(',', '.').replace(u'\xa0', u''))
    base['Владелец'] = i['Владелец']
    sql.execute("INSERT INTO Upload1C_fuelbase (storage, fuel, balance, owner, date) VALUES (?,?,?,?,?)",
                (base['Склад'], base['Номенклатура'], base['КонечныйОстаток'], base['Владелец'], current_date))
    db.commit()
