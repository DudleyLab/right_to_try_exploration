
#it's a lot harder to read regex then write it
from Lexicon import Lexicon
import re




class DrugLexicon(Lexicon):

    def processLine(self, line):
            #pattern = re.compile(">[^,'\"]+|(['\"])(>[^\"'\\\\]+\\\\.|(?!\\1)[\"'])*\\1|(?<=,|^)\\s*(?=,|$)")
            splitLine = line.split("\t")
            pgkbId = splitLine[0]
            mainName = splitLine[1]
            prelimOtherNames = []
            otherNames = []

            prelimOtherNames.append(splitLine[2])
            prelimOtherNames.append(splitLine[3])
            #print("hi")
            #if splitLine[2] != None:
            #    print(pattern.findall(splitLine[2]))
                
            #if splitLine[3] != None:
            #    print(re.match(">[^,'\"]+|(['\"])(>[^\"'\\\\]+\\\\.|(?!\\1))", splitLine[3]))

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
                    self.processLine(inputLine.replace(" ", ""))
            except:
                print("file reading error")

    def DrugLexicon(self, inputStream):
        self.readFromInputStream(inputStream)
drugs = DrugLexicon()
drugs.DrugLexicon("drug-lexicon-sample.tsv")
for x in sorted(drugs.allTerms, key=len):
    print(x)
print(len(sorted(drugs.allTerms, key=len)))

