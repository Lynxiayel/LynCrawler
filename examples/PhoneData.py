import re
import ast

class PhoneData:
    def __init__(self,file='phone_specs.txt'):
        self.data=[]
        with open(file, 'r') as f:
            for i in f.readlines():
                self.data.append(dict(ast.literal_eval(i)))

    def getDate(self):
        monthDict = dict({'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12})
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        monthPat = re.compile('(' + '|'.join(months) + ')', re.IGNORECASE)
        yearPat = re.compile(r'(\d+)')
        result=[]
        for i in self.data:
            date = i['announceDate'][0].split(', ')
            if len(date) >= 2 :
                year = yearPat.findall(date[0])
                if year:
                    year=year[0]
                else:
                    year='0'
                month = monthPat.findall(date[1])
                if month:
                    month=str(monthDict[month[0]])
                else:
                    month='0'
            elif len(date)==1:
                month='0'
                year = yearPat.findall(date[0])
                if year:
                    year=year[0]
                else:
                    year='0'
            else:
                year='0'
                month='0'
            tmp=year+'.'+month
            result.append(float(tmp))
        return result


    def getName(self):
        name=[]
        for i in self.data:
            if i['name']:
                name.append(i['name'][0])
            else:
                name.append('')
        return name

    def getSize(self):
        sizePat = re.compile(r'([\d.]+?) inches')
        size=[]
        for i in self.data:
            if i['size']:
                tmp=sizePat.findall(i['size'][0])
                if tmp:
                    size.append(float(tmp[0]))
                else:
                    size.append(0)
            else:
                size.append(0)
        return size

    def getBrand(self):
        brandPat = re.compile(r'(\w+?) ')
        brand=[]
        for i in self.data:
            if i['name']:
                tmp=brandPat.findall(i['name'][0])
                if tmp:
                    brand.append(tmp[0])
                else:
                    brand.append('')
            else:
                brand.append('')
        return brand

    def getBattery(self):
        batPat = re.compile(r'(\d+?) mAh', re.IGNORECASE)
        battery=[]
        for i in self.data:
            if i['battery']:
                tmp=batPat.findall(i['battery'][0])
                if tmp:
                    battery.append(int(tmp[0]))
                else:
                    battery.append(0)
            else:
                battery.append(0)
        return battery

if __name__=='__main__':
    data=PhoneData()
    bat=data.getBattery()
    brand=data.getBrand()
    date=data.getDate()
    name=data.getName()
    size=data.getSize()
    print len(name),len(date),len(size), len(brand),len(bat)
#with open('phone_specs.txt', 'r') as f:
#    s = []
#    for i in f.readlines():
#        s.append(dict(ast.literal_eval(i)))
#months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
#monthPat = re.compile('(' + '|'.join(months) + ')', re.IGNORECASE)
#yearPat = re.compile(r'(\d+)')
#batPat = re.compile(r'(\d+?) mAh', re.IGNORECASE)
#brandPat = re.compile(r'(\w+?) ')
#sizePat = re.compile(r'([\d.]+?) inches')
#with open('battery.txt', 'w') as b:
#    for i in s:
#        date = i['announceDate'][0].split(', ')
#        bat = i['battery']
#        name = i['name']
#        stand_by=i['stand-by']
#        stand_by_2g=i['stand-by-2g']
#        stand_by_3g=i['stand-by-3g']
#        size = i['size']
#        if len(date) >= 2 and len(bat) >= 1:
#            year = yearPat.findall(date[0])
#            month = monthPat.findall(date[1])
#            bat = batPat.findall(bat[0])
#            brand = brandPat.findall(name[0])
#            size = sizePat.findall(size[0])
#            if month and year and bat and brand and size:
#                b.write(name[0]+' '+year[0] + '.' + str(monthDict[month[0]]) + ' ' + bat[0] + ' ' + size[0] + ' ' + brand[0] + '\n')
