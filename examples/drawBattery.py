import numpy as np
from numpy.random import randn
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("deep", desat=.6)
from PhoneData import PhoneData


def sortCorrelatedData(*args):
    '''sort correlated data given in list1, list2,...
        list1 is used as the key for sorting defaultly
    '''
    tups=zip(*args)
    tups.sort()
    return zip(*tups)

def excludeTablet(index,size,*args):
    '''exclude tablet(screenSize>size)
        index denotes the position of the size-list in *args
    '''
    tups=zip(*args)
    idxToDel=[]
    for i,v in enumerate(tups):
        if v[index]>size:
            idxToDel.append(i)
    idxToDel.sort(reverse=True)
    for i in idxToDel:
        tups.pop(i)
    return zip(*tups)

def excludeEmptyEntry(*args):
    tups=zip(*args)
    idxToDel=[]
    for i,v in enumerate(tups):
        for j in v:
            if j==0 or j=='':
                idxToDel.append(i)
                break
    idxToDel.sort(reverse=True)
    for i in idxToDel:
        tups.pop(i)
    return zip(*tups)

def extractByBrand(index,brand,*args):
    '''extract only the data of a specific brand
        index indicates the position of the brand-list in *args
    '''
    brand=brand.lower()
    tups=zip(*args)
    hitIdx=[]
    for i,v in enumerate(tups):
        if v[index].lower()==brand:
            hitIdx.append(i)
    hitIdx.sort(reverse=True)
    result=[]
    for i in hitIdx:
        result.append(tups.pop(i))
    return zip(*result)





if __name__=='__main__':
    data=PhoneData()
    date=data.getDate()
    bat=data.getBattery()
    size=data.getSize()
    brand=data.getBrand()
    name=data.getName()
    sdb2=data.getStandBy2G()
    #the following loop is to remove incorrectly crawled stand-by time, no need in future refined version
    for i,v in enumerate(sdb2):
        if v<40:
           sdb2[i]=0

    date,size,brand,name,bat,sdb2=excludeEmptyEntry(date,size,brand,name,bat,sdb2)
    date,size,brand,name,bat,sdb2=sortCorrelatedData(date,size,brand,name,bat,sdb2)
    date,size,brand,name,bat,sdb2=excludeTablet(1,6.9,date,size,brand,name,bat,sdb2)
    #date,size,brand,name,bat,sdb2=extractByBrand(2,'SamSung',date,size,brand,name,bat,sdb2)
    print zip(date,name,sdb2)
    plt.plot(date,bat)
    plt.plot(date,sdb2)
    plt.show()
