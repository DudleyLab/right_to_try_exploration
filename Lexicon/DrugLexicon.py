
from Lexicon import Lexicon




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
                if (name != ''):
                    for names in name.split(',"'):
                        parsed_name = names.replace('"','')
                        if(parsed_name != mainName and parsed_name not in otherNames):
                            otherNames.append(parsed_name)
            self.addLineDataToMaps(mainName, pgkbId, otherNames, None)          




    def readFromInputStream(self, lexiconInputStream):
        with open(lexiconInputStream) as fp:
            lines = fp.readlines()
            try:
                for inputLine in lines[1:]:
                    self.processLine(inputLine)
            except:
                print("file reading error")

    def DrugLexicon(self, inputStream):
        self.readFromInputStream(inputStream)

drugs = DrugLexicon()
drugs.DrugLexicon("drugs.tsv")
drugs.getUses()
