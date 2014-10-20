import re
import ast

with open('phone_specs.txt', 'r') as f:
    s = []
    for i in f.readlines():
        s.append(dict(ast.literal_eval(i)))
monthDict = dict(
    {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
     'Oct': 10, 'Nov': 11, 'Dec': 12})
# for i in s:
# j=i['announceDate'][0].split(', ')
# print j[0],month[j[1]], i['battery']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
monthPat = re.compile('(' + '|'.join(months) + ')', re.IGNORECASE)
yearPat = re.compile(r'(\d+)')
batPat = re.compile(r'(\d+?) mAh', re.IGNORECASE)
brandPat = re.compile(r'(\w+?) ')
sizePat = re.compile(r'([\d.]+?) inches')
with open('battery.txt', 'w') as b:
    for i in s:
        date = i['announceDate'][0].split(', ')
        bat = i['battery']
        name = i['name']
        stand_by=i['stand-by']
        stand_by_2g=i['stand-by-2g']
        stand_by_3g=i['stand-by-3g']
        size = i['size']
        if len(date) >= 2 and len(bat) >= 1:
            year = yearPat.findall(date[0])
            month = monthPat.findall(date[1])
            bat = batPat.findall(bat[0])
            brand = brandPat.findall(name[0])
            size = sizePat.findall(size[0])
            if month and year and bat and brand and size:
                b.write(name[0]+' '+year[0] + '.' + str(monthDict[month[0]]) + ' ' + bat[0] + ' ' + size[0] + ' ' + brand[0] + '\n')
