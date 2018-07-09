
#it's a lot harder to read regex then write it
from Lexicon import Lexicon
import pandas as pd
import re



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




            #both matcher parts literally just regex to parse drugs out of Generic Names and Trade Names
            #basically reading shit in line by line and then parsing out names 
            #need to figure out   addLineDataToMaps(mainName, pgkbId, otherNames, null);

drugs = DrugLexicon()
#drugs.readFromInputStream('drugs.tsv')
drugs.readFromInputStream('drug-lexicon-sample.tsv')
print(len(drugs.getAllTerms()))
print(drugs.containsTerm("1,7-dimethylxanthine"))
print(drugs.containsTerm("paraxanthine"))
print(drugs.containsTerm("MEDR-640"))
print(drugs.containsTerm("Adinazolamum [INN-Latin]"))
print(drugs.containsTerm("T-cell growth factor"))
print(drugs.containsTerm("Proleukin"))
print(drugs.containsTerm("Aldose reductase inhibitors"))
print(drugs.containsTerm(""))

