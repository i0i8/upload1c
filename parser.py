import json
import sqlite3
from datetime import date

current_date = date.today()

db = sqlite3.connect('db.sqlite3')
sql = db.cursor()
# sql.execute(""" CREATE TABLE IF NOT EXISTS opt(
#             month DATE,
#             type_sale TEXT,
#             type_oil TEXT,
#             value_month FLOAT,
#             value_quarter FLOAT,
#             value_year FLOAT,
#             value_fact_month FLOAT,
#             value_fact_quarter FLOAT,
#             value_fact_year FLOAT,
#             value_fact_previous_month FLOAT
# ); """)
# sql.execute("""CREATE TABLE IF NOT EXISTS retail(
#             month DATE,
#             type_sale TEXT,
#             type_oil TEXT,
#             value_month FLOAT,
#             value_quarter FLOAT,
#             value_year FLOAT,
#             value_fact_month FLOAT,
#             value_fact_quarter FLOAT,
#             value_fact_year FLOAT,
#             value_fact_previous_month FLOAT)""")
# db.commit()

with open("1.json", 'r', encoding='utf-8-sig') as f:
    read = f.read()


data = json.loads(read)

opt = {}
retail = {}
for i in data['data']:
    if i['ВидПродаж'] == 'ОПТ':
        if i['ВидТоплива'] == '':
            opt['ВидТоплива'] = 'Топливо не указано'
        else:
            opt['ВидТоплива'] = i['ВидТоплива']

        if i['СуммаМесяц'] == '':
            opt['СуммаМесяц'] = 0
        else:
            opt['СуммаМесяц'] = float(
                i['СуммаМесяц'].replace(',', '.').replace(u'\xa0', u''))

        if i['СуммаКвартал'] == '':
            opt['СуммаКвартал'] = 0
        else:
            opt['СуммаКвартал'] = float(
                i['СуммаКвартал'].replace(',', '.').replace(u'\xa0', u''))

        if i['СуммаГод'] == '':
            opt['СуммаГод'] = 0
        else:
            opt['СуммаГод'] = float(i['СуммаГод'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактМесяц'] == '':
            opt['СуммаФактМесяц'] = 0
        else:
            opt['СуммаФактМесяц'] = float(i['СуммаФактМесяц'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактКвартал'] == '':
            opt['СуммаФактКвартал'] = 0
        else:
            opt['СуммаФактКвартал'] = float(i['СуммаФактКвартал'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактГод'] == '':
            opt['СуммаФактГод'] = 0
        else:
            opt['СуммаФактГод'] = float(i['СуммаФактГод'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактПредМесяц'] == '':
            opt['СуммаФактПредМесяц'] = 0
        else:
            opt['СуммаФактПредМесяц'] = float(
                i['СуммаФактПредМесяц'].replace(',', '.').replace(u'\xa0', u''))
        opt['unitate'] = 'тн'
        sql.execute("INSERT INTO Upload1C_smallopt (typeOil, summMonth, summQuarter, summYear, summFactMonth, summFactQuarter, summFactYear, summFactBeforeMonth, date, unitate) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (opt['ВидТоплива'], opt['СуммаМесяц'], opt['СуммаКвартал'], opt['СуммаГод'], opt['СуммаФактМесяц'], opt['СуммаФактКвартал'],
                     opt['СуммаФактГод'], opt['СуммаФактПредМесяц'], current_date, opt['unitate']))
        db.commit()
    if i['ВидПродаж'] == 'Розница':
        if i['ВидТоплива'] == '':
            retail['ВидТоплива'] = 'Топливо не указано'
        else:
            retail['ВидТоплива'] = i['ВидТоплива']

        if i['СуммаМесяц'] == '':
            retail['СуммаМесяц'] = 0
        else:
            retail['СуммаМесяц'] = float(
                i['СуммаМесяц'].replace(',', '.').replace(u'\xa0', u''))

        if i['СуммаКвартал'] == '':
            retail['СуммаКвартал'] = 0
        else:
            retail['СуммаКвартал'] = float(
                i['СуммаКвартал'].replace(',', '.').replace(u'\xa0', u''))

        if i['СуммаГод'] == '':
            retail['СуммаГод'] = 0
        else:
            retail['СуммаГод'] = float(i['СуммаГод'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактМесяц'] == '':
            retail['СуммаФактМесяц'] = 0
        else:
            retail['СуммаФактМесяц'] = float(i['СуммаФактМесяц'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактКвартал'] == '':
            retail['СуммаФактКвартал'] = 0
        else:
            retail['СуммаФактКвартал'] = float(i['СуммаФактКвартал'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактГод'] == '':
            retail['СуммаФактГод'] = 0
        else:
            retail['СуммаФактГод'] = float(i['СуммаФактГод'].replace(
                ',', '.').replace(u'\xa0', u''))

        if i['СуммаФактПредМесяц'] == '':
            retail['СуммаФактПредМесяц'] = 0
        else:
            retail['СуммаФактПредМесяц'] = float(
                i['СуммаФактПредМесяц'].replace(',', '.').replace(u'\xa0', u''))
        retail['unitate'] = 'тн'
        sql.execute("INSERT INTO Upload1C_retailvalue (typeOil, summMonth, summQuarter, summYear, summFactMonth, summFactQuarter, summFactYear, summFactBeforeMonth, date, unitate) VALUES (?,?,?,?,?,?,?,?,?,?)", (retail['ВидТоплива'],
                    retail['СуммаМесяц'], retail['СуммаКвартал'], retail['СуммаГод'], retail['СуммаФактМесяц'], retail['СуммаФактКвартал'],
                    retail['СуммаФактГод'], retail['СуммаФактПредМесяц'], current_date, retail['unitate']))
        db.commit()

sql.execute(f"INSERT INTO Upload1C_datelink (date) VALUES (?)", (current_date,))
db.commit()
