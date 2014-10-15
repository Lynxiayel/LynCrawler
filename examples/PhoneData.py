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
        yearPat = re.compile(r'(\d+)$')
        result=[]
        for i in self.data:
            date = i['announceDate'][0].split(', ')
            if len(date) >= 2 :
                if 'Q' in date[0]:#incase of date string like'1Q, 2003'
                    year = yearPat.findall(date[1])
                else:
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
        batPat = re.compile(r'([\d,]+?) mAh', re.IGNORECASE)
        battery=[]
        for i in self.data:
            if i['battery']:
                tmp=batPat.findall(i['battery'][0])
                if tmp:
                    battery.append(int(tmp[0].replace(',','')))
                else:
                    battery.append(0)
            else:
                battery.append(0)
        return battery

    def getStandBy(self):
        sdb=[]
        for i in self.data:
            if i['stand-by']:
                sdb.append(int(i['stand-by'][0]))
            else:
                sdb.append(0)
        return sdb

    def getStandBy2G(self):
        sdb=[]
        for i in self.data:
            if i['stand-by-2g']:
                sdb.append(int(i['stand-by-2g'][0]))
            else:
                sdb.append(0)
        return sdb

    def getStandBy3G(self):
        sdb=[]
        for i in self.data:
            if i['stand-by-3g']:
                sdb.append(int(i['stand-by-3g'][0]))
            else:
                sdb.append(0)
        return sdb

if __name__=='__main__':
    data=PhoneData()
    bat=data.getBattery()
    brand=data.getBrand()
    date=data.getDate()
    name=data.getName()
    size=data.getSize()
    sdb=data.getStandBy()
    sdb2=data.getStandBy2G()
    sdb3=data.getStandBy3G()
    print zip(name,sdb,sdb2, sdb3)
