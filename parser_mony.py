import json
import sqlite3
from datetime import date

current_date = date.today()

db = sqlite3.connect('db.sqlite3')
sql = db.cursor()

with open("json/3.json", 'r', encoding='utf-8-sig') as f:
    read = f.read()

data = json.loads(read)

mony = {}
print(current_date)
for i in data['data']:
    if i['СуммаДень'] == '':
        mony['СуммаДень'] = 0
    else:
        mony['СуммаДень'] = float(
            i['СуммаДень'].replace(',', '.').replace(u'\xa0', u''))
    mony['Организация'] = i['Организация']
    mony['ВидПродаж'] = i['ВидПродаж']
    if i['СуммаМесяц'] == '':
        mony['СуммаМесяц'] = 0
    else:
        mony['СуммаМесяц'] = float(
            i['СуммаМесяц'].replace(',', '.').replace(u'\xa0', u''))
    if i['СуммаГод'] == '':
        mony['СуммаГод'] = 0
    else:
        mony['СуммаГод'] = float(i['СуммаГод'].replace(
            ',', '.').replace(u'\xa0', u''))
    sql.execute("INSERT INTO Upload1C_mony (unitate, summDay, owner, typeSela, summMonth, summYear, date) VALUES (?,?,?,?,?,?,?)",
                ('т.руб', mony['СуммаДень'], mony['Организация'], mony['ВидПродаж'], mony['СуммаМесяц'], mony['СуммаГод'], current_date))
    db.commit()
