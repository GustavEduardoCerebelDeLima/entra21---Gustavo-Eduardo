import arrow

data = arrow.now().format('DD/MM/YYYY')
print(data)
data = arrow.now().format('HH:mm')
print(data)
data = arrow.get(25)
print(data)
date_1 = arrow.get('2022-07-14 18:40:48','YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2005-08-17 13:18:20','YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)
