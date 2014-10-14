__author__ = 'lynxiayel'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from LynCrawler import LynCrawler
import re

if __name__ == '__main__':
    crawler = LynCrawler()

    ######### Data items to analyze
    ###### name
    namePat = re.compile(r'''<h1>(.+?)</h1>''', re.DOTALL)
    crawler.addPageAnalyzeItem('name', namePat)
    ###### chipset
    chipsetPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=chipset">Chipset</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('chipset', chipsetPat)
    ###### CPU
    cpuPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=cpu">CPU</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('cpu', cpuPat)
    ###### Internal memory
    memPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=dynamic-memory">Internal</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('memory', memPat)
    ###### GPU
    gpuPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=gpu">GPU</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('gpu', gpuPat)
    ###### sensor
    sensorPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=sensors">Sensors</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('sensor', sensorPat)
    ###### GPS
    gpsPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=gps">GPS</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('gps', gpsPat)
    ###### battery
    batteryPat = re.compile(r'''<th rowspan="3" scope="row">Battery</th>.
<td class="ttl">&nbsp;</td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('battery', batteryPat)
    ###### announce date
    announceDatePat = re.compile(r'''<td class="ttl"><a href=# onClick="helpW\('h_year\.htm'\);">Announced</a></td>.*?
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('announceDate', announceDatePat)
    ###### screen size
    sizePat = re.compile(r'''<td class="ttl"><a href=# onClick="helpW\('h_dsize\.htm'\);">Size</a></td>.*?
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('size', sizePat)
    ###### weight
    weightPat = re.compile(r'''<td class="ttl"><a href=# onClick="helpW\('h_weight\.htm'\);">Weight</a></td>.*?
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('weight', weightPat)
    ###### Primary camera
    pCameraPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=camera">Primary</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('pCamera', pCameraPat)
     ###### bluetooth
    btPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=bluetooth">Bluetooth</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('bluetooth', btPat)
    ###### dimensions
    dimPat = re.compile(r'''<td class="ttl"><a href=# onClick="helpW\('h_dimens\.htm'\);">Dimensions</a></td>.*?
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('dimensions', dimPat)
    ###### multitouch
    mtPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=multitouch">Multitouch</a></td>.
<td class="nfo">(.+?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('multitouch', mtPat)
    ###### stand-by time (not given 2g or 3g)
    sbtPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=stand-by-time">Stand-by</a></td>[.]?
<td class="nfo">Up to ([\d]+?) h</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('stand-by', sbtPat)
    ###### stand-by time 2G
    sbt2Pat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=stand-by-time">Stand-by</a></td>[.]?
<td class="nfo">Up to ([\d]+?) h \(2G\).*?</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('stand-by-2g', sbt2Pat)
    ###### stand-by time 3G
    sbt3Pat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=stand-by-time">Stand-by</a></td>[.]?
<td class="nfo">.*?Up to ([\d]+?) h \(3G\)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('stand-by-3g', sbt3Pat)
    ###### NFC
    nfcPat = re.compile(r'''<td class="ttl"><a href="glossary\.php3\?term=nfc">NFC</a></td>.*?
<td class="nfo">(.*?)</td>''', re.DOTALL)
    crawler.addPageAnalyzeItem('nfc', nfcPat)

    ######### Url sniff item
    pat1 = re.compile(r'''<a href=(.+?\.php)>[\d\w]+?</a>''', )
    crawler.addPageSniffItem('newPage', pat1)
    pat2 = re.compile(r'''<a href="(.+?\.php)">[\d\w\W]+?</a>''', )
    crawler.addPageSniffItem('newPage2', pat2)

    ######### crawl
    crawler.start('http://www.gsmarena.com/htc_desire_820_dual_sim-6637.php')
