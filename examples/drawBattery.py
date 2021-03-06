import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("deep", desat=.6)
from PhoneData import PhoneData


def sortCorrelatedData(*args):
    '''sort correlated data given in list1, list2,...
        list1 is used as the key for sorting defaultly
    '''
    tups = zip(*args)
    tups.sort()
    return zip(*tups)


def excludeTablet(index, size, *args):
    '''exclude tablet(screenSize>size)
        index denotes the position of the size-list in *args
    '''
    tups = zip(*args)
    idxToDel = []
    for i, v in enumerate(tups):
        if v[index] > size:
            idxToDel.append(i)
    idxToDel.sort(reverse=True)
    for i in idxToDel:
        tups.pop(i)
    return zip(*tups)


def excludeEmptyEntry(*args):
    tups = zip(*args)
    idxToDel = []
    for i, v in enumerate(tups):
        for j in v:
            if j == 0 or j == '' or j is None:
                idxToDel.append(i)
                break
    idxToDel.sort(reverse=True)
    for i in idxToDel:
        tups.pop(i)
    return zip(*tups)


def extractByBrand(index, brand, *args):
    '''extract only the data of a specific brand
        index indicates the position of the brand-list in *args
    '''
    brand = brand.lower()
    tups = zip(*args)
    hitIdx = []
    for i, v in enumerate(tups):
        if v[index].lower() == brand:
            hitIdx.append(i)
    hitIdx.sort(reverse=True)
    result = []
    for i in hitIdx:
        result.append(tups.pop(i))
    return zip(*result)


def saveAvg(date, value, filename):
    avg = {}
    for d, b in zip(date, value):
        d = int(d)  # if do not want the year-wise average, comment this line
        if d in avg.keys():
            avg[d].append(b)
        else:
            avg[d] = [b]
    keys = sorted(avg)
    if os.path.isfile(filename):
        os.remove(filename)

    with open(filename, 'a') as f:
        for k in keys:
            v = sum(avg[k]) / len(avg[k])
            f.write(str(k) + ', ' + str(v) + '\n')


if __name__ == '__main__':
    data = PhoneData()
    date = data.getDate()
    bat = data.getBattery()
    size = data.getSize()
    brand = data.getBrand()
    name = data.getName()
    sdb = data.getStandBy()
    sdb2 = data.getStandBy2G()
    sdb3 = data.getStandBy3G()
    # the following loop is to remove incorrectly crawled stand-by time, no
    # need in future refined version
    for i, v in enumerate(sdb2):
        if v < 40:
            sdb2[i] = 0

    # date,size,brand,name,bat,sdb2=extractByBrand(2,'SamSung',date,size,brand,name,bat,sdb2)
    # plot date-battery
    date, bat, size = excludeTablet(2, 6.9, date, bat, size)
    date, bat = excludeEmptyEntry(date, bat)
    date, bat = sortCorrelatedData(date, bat)
    #print "number of devices in graph", len(date)
    plt.scatter(date, bat, s=34, alpha=0.5)
    plt.xlabel('Released date of the device', fontsize='26')
    plt.xticks(fontsize='20')
    plt.ylabel('Battery compacity (mAh)', fontsize='26')
    plt.yticks(fontsize='20')
    ax = plt.gca()
    fmt = mpl.ticker.ScalarFormatter(useOffset=False)
    fmt.set_scientific(False)
    ax.set_ylim([0, 4400])
    ax.set_xlim([1996.5, 2015.3])
    ax.xaxis.set_major_formatter(fmt)
    a, b, c, d, e = np.polyfit(date, bat, 4)
    plotdate = np.array(date)
    plt.plot(plotdate, a * plotdate ** 4 + b * plotdate **
             3 + c * plotdate ** 2 + d * plotdate + e, color='r')
    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    fig.savefig('date-battery', dpi=300)
    plt.close()

    # plot date-stand-by
    date1, sdb, size = excludeTablet(2, 6.9, date, sdb, size)
    date1, sdb = excludeEmptyEntry(date1, sdb)
    date1, sdb = sortCorrelatedData(date1, sdb)
    date2, sdb2, size = excludeTablet(2, 6.9, date, sdb2, size)
    date2, sdb2 = excludeEmptyEntry(date2, sdb2)
    date2, sdb2 = sortCorrelatedData(date2, sdb2)
    date3, sdb3, size = excludeTablet(2, 6.9, date, sdb3, size)
    date3, sdb3 = excludeEmptyEntry(date3, sdb3)
    date3, sdb3 = sortCorrelatedData(date3, sdb3)
    # print "number of devices in graph", len(date)
    plt.scatter(
        date1, sdb, s=36, linewidth=2, color='g', marker='+', label='stand-by', alpha=0.5)
    plt.scatter(date2, sdb2, s=32, color='b', marker='o',
                label='stand-by-2g', alpha=0.5)
    plt.scatter(date3, sdb3, s=36, linewidth=2, color='k',
                marker='x', label='stand-by-3g', alpha=0.5)
    plt.xlabel('Released date of the device', fontsize='26')
    plt.xticks(fontsize='20')
    plt.ylabel('Stand-by time (h)', fontsize='26')
    plt.yticks(fontsize='20')
    ax = plt.gca()
    fmt = mpl.ticker.ScalarFormatter(useOffset=False)
    fmt.set_scientific(False)
    ax.xaxis.set_major_formatter(fmt)
    ax.set_ylim([0, 1550])
    ax.set_xlim([1996.5, 2015.3])
    ax.legend(fontsize=20, loc='upper left')
    a, b, c, d, e = np.polyfit(date1, sdb, 4)
    a2, b2, c2, d2, e2 = np.polyfit(date2, sdb2, 4)
    a3, b3, c3, d3, e3 = np.polyfit(date3, sdb3, 4)
    plotdate1 = np.array(date1)
    plotdate2 = np.array(date2)
    plotdate3 = np.array(date3)
    plt.plot(plotdate1, a * plotdate1 ** 4 + b * plotdate1 **
             3 + c * plotdate1 ** 2 + d * plotdate1 + e, color='g')
    plt.plot(plotdate2, a2 * plotdate2 ** 4 + b2 * plotdate2 **
             3 + c2 * plotdate2 ** 2 + d2 * plotdate2 + e2, color='b')
    plt.plot(plotdate3, a3 * plotdate3 ** 4 + b3 * plotdate3 **
             3 + c3 * plotdate3 ** 2 + d3 * plotdate3 + e3, color='k')
    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    fig.savefig('date-sdb', dpi=300)
    plt.close()

    # save average bat and sdb
    saveAvg(date, bat, 'avgBattery.txt')
    saveAvg(date1, sdb, 'avgSdb.txt')
    saveAvg(date2, sdb2, 'avgSdb2.txt')
    saveAvg(date3, sdb3, 'avgSdb3.txt')
