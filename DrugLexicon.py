
#it's a lot harder to read regex then write it
from Lexicon import Lexicon
import pandas as pd
import re
import unittest



class DrugLexicon(Lexicon):

    def processLine(self, line):
            splitLine = line.split("\t")
            pgkbId = splitLine[0]
            mainName = splitLine[1]
            prelimOtherNames = []
            otherNames = []

            prelimOtherNames.append(splitLine[2])
            prelimOtherNames.append(splitLine[3])

            for name in prelimOtherNames:
                if name != '':
                    for names in name.split(','):
                        otherNames.append(names.replace('"',''))
            self.addLineDataToMaps(mainName, pgkbId, otherNames, None);




    def readFromInputStream(self, lexiconInputStream):
        with open(lexiconInputStream) as fp:
            lines = fp.readlines()
            try:
                for inputLine in lines[1:]:
                    self.processLine(inputLine)
            except:
                print("file reading error")

#playing more with regex
drugs = DrugLexicon()
drugs.readFromInputStream('drug-lexicon-sample.tsv')
print(drugs.getAllTerms())