__author__ = 'lynxiayel'
import re


class Analyzer:

    def __init__(self):
        self.items = {}

    def addItem(self, name, reStr):
        self.items.update({name: reStr})

    def rmItem(self, name):
        self.items.pop(name)

    def updateItem(self, name, reStr):
        self.items.update({name: reStr})

    def analyzeItem(self, targetStr, pat):
        result = pat.findall(targetStr)
        return result

    def analyzeItemGroup(self, targetStr, names):
        result = {}
        for name in names:
            result[name] = self.analyzeItem(targetStr, name)
        return result

    def analyzeAll(self, targetStr):
        result = {}
        for name in self.items.keys():
            result[name] = self.analyzeItem(targetStr, self.items.get(name))
        return result

    def getItemCount(self):
        return len(self.items)
