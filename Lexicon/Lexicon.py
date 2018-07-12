class Lexicon():
    def __init__(self):
    	self.termToMainNameMap = {}
    	self.termToIdMap = {}
        #values of dicts not being perseved values of lists are idk y
    	self.idToMainNameMap = {}
    	self.synonymMap = {}
    	self.allTerms = []
    	self.allTermsLowerCase = []
    	self.allTermsWhitespaceTokenized = []
    	self.parentMap = {}
    	self.nRecords = 0

    def addLineDataToMaps(self, mainName, id, otherNames, parents):
        self.allTerms.append(mainName)
        self.allTermsLowerCase.append(mainName.lower())
        for term in mainName.split(' '):
            self.allTermsWhitespaceTokenized.append(term)
        self.termToMainNameMap[mainName] = mainName
        self.termToMainNameMap[mainName.lower()] = mainName
        self.termToIdMap[mainName] = id
        self.idToMainNameMap[id] = mainName
        self.synonymMap.setdefault(mainName, [])
        self.synonymMap.setdefault(mainName, []).append(mainName)

        self.nRecords = self.nRecords + 1

        for otherName in otherNames:
            self.termToMainNameMap[otherName] = mainName
            self.termToMainNameMap[otherName.lower()] = mainName
            self.allTerms.append(otherName)
            self.allTermsLowerCase.append(otherName.lower())
            for term in otherName.split(' '):
                self.allTermsWhitespaceTokenized.append(term)
            self.synonymMap.setdefault(mainName, []).append(otherName)


            #parent stuff not appliacable for drug application


     
    def containsTerm(self, term):
        return term in self.allTerms

    def containsTermLowerCase(self, term):
    	return term.lower() in self.allTermsLowerCase

    def getAllMainTerms(self):
    	return self.termToIdMap.values()

    def getAllTerms(self):
    	return list(set(self.allTerms))

    def getAllTermsLowerCase(self):
    	return list(set(self.allTermsLowerCase))

    def getAllTermsWhitespaceTokenized(self):
    	return self.allTermsWhitespaceTokenized

    def getnRecords(self):
    	return self.nRecords

    def getMainNameForTerm(self, term):
    	if(term not in self.allTerms):
    		return None
    	return self.termToMainNameMap.get(term)

    def getMainNameForId(self, id):
        if(id not in self.idToMainNameMap):
            return None
        return self.idToMainNameMap.get(id)

            
       
        '''
    	if(id not in self.idToMainNameMap.keys()):
    		return self.idToMainNameMap
    	return idToMainNameMap.get(id)
        '''

    def getSynonyms(self, term):
        mainName = self.getMainNameForTerm(term)
        if(mainName not in self.synonymMap):
            return None
        return self.synonymMap.get(mainName)


    #double check this one not sure if handling null's conversion from java code right
    #check if the default or stuff is working
    def getId(self, term):
        if (self.containsTermLowerCase(term) == None):
            return None
        mainName = self.termToMainNameMap[term.lower()]
        return self.termToIdMap[mainName]

    def getParents(self, myId):
        if(myId not in self.parentMap):
            return []
        parentIds = parentMap.get(myId)
        parents = []
        for p_id in parentIds:
            parents.append(p_id)
            for id in getParents(p_id):
                parents.append(id)
        return parents

    def getAncestors(self, name):
        id = getId(name)
        if (id == None):
            return None
        return getParents(id)

    #formating stuff didn't convert
    def getSynonymsLowercaseConcatenated(self, term):
        mainName = getMainNameForTerm(term)
        if(mainName not in self.synonymMap):
            return None
        synmap = synonymMap.get(mainName)
        formattedSynonyms = []
        for synonym in synmap:
            formattedSynonyms.append(synonym.lower().replace(' ', '_'))
        return formattedSynonyms

    def getPipeSeparatedTermsById(self):
    	f = open('drugs_r.tsv', 'w')
    	f.write("PharmagkbID\tDrug Names\n")
    	for id in self.idToMainNameMap:
    		mainName = self.getMainNameForId(id)
    		terms = self.getSynonyms(mainName)
    		f.write("%s\t%s\n" %(id, "|".join([str(x) for x in self.getSynonyms(mainName)])))
    	f.close()

    		



    def readFromInputStream(self, inputStream):
        raise NotImplementedError("Python doesn't have abstract classes")

