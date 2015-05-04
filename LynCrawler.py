__author__ = 'lynxiayel'
from Analyzer import Analyzer
import mechanize


class LynCrawler:

    def __init__(self):
        self.ToCrawl = set([])
        self.Crawled = set([])
        self.Crawling = ""
        self.PageAnalyzer = Analyzer()  # used to extract useful info
        self.PageSniffer = Analyzer()  # used to find new pages to crawl
        self.initBrowser()

    def initBrowser(self):
        self.browser = mechanize.Browser()
        # important to bypass the website anti-robot defence
        self.browser.set_handle_robots(False)
        self.browser.addheaders = [("User-Agent",
                                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")]

    def addPageSniffItem(self, name, reStr):
        self.PageSniffer.addItem(name, reStr)

    def rmPageSniffItem(self, name):
        self.PageSniffer.rmItem(name)

    def addPageAnalyzeItem(self, name, reStr):
        self.PageAnalyzer.addItem(name, reStr)

    def rmPageAnalyzeItem(self, name):
        self.PageAnalyzer.rmItem(name)

    def sniffNewPage(self, pageContent):
        if self.PageSniffer.getItemCount() == 0:
            print "No sniff items yet. Please add new items use addPageSniffItem()."
        else:
            result = []
            for i in self.PageSniffer.analyzeAll(pageContent).values():
                if i:
                    for p in i:
                        if p:
                            newPage = self.generateNewPageURL(p)
                        result.append(newPage)
            for p in result:
                if p not in self.Crawled:
                    self.ToCrawl.add(p)

    def analyzePage(self, pageContent):
        if self.PageAnalyzer.getItemCount() == 0:
            print "No data items for analyzing yet. Please add new items use addPageAnalyzeItem()."
        else:
            return self.PageAnalyzer.analyzeAll(pageContent)

    def start(self, initPage):
        self.ToCrawl.add(initPage)
        while self.ToCrawl:
            self.crawl(self.ToCrawl.pop())
        else:
            print "All done."
            return True

    def crawl(self, page):
        try:
            response = self.browser.open(page)
            pageContent = response.read()
            self.store(self.analyzePage(pageContent))
            self.Crawled.add(page)
            print 'page crawled:', page
            self.sniffNewPage(pageContent)
        except Exception as e:
            print e.message
            print "something went wrong when crawling ", page

    def store(self, data):
        with open('data.txt', 'a+') as f:
            f.write(str(data))
            f.write("\n")

    def generateNewPageURL(self, tmpURL, parentPath=""):
        """Sometimes the new url sniffed from the page content are relative path, you can modify it here."""
        if not parentPath:
            parPath = r"http://www.gsmarena.com/"
        if "http://" in tmpURL:
            return tmpURL
        else:
            return parPath + tmpURL
