'''
Based off Dr. Percha's code
'''
class Lexicon():
    def __init__(self):
    	self.termToMainNameMap = {}
    	self.termToIdMap = {}
    	self.idToMainNameMap = {}
    	self.synonymMap = {}
    	self.allTerms = {}
    	self.allTermsLowerCase = {'hi'}
    	self.allTermsWhitespaceTokenized = {}
    	self.parentMap = {}
    	self.nRecords = 0
     
    def containsTerm(self, term):
        return term in self.allTerms.values()

    def containsTermLowerCase(self, term):
    	return term.lower() in self.allTermsLowerCase

    def getAllMainTerms(self):
    	return self.termToIdMap.keys()

    def getAllTerms(self):
    	return self.allTerms

    def getAllTermsLowerCase(self):
    	return self.allTermsLowerCase

    def getAllTermsWhitespaceTokenized(self):
    	return self.allTermsWhitespaceTokenized

    def getnRecords(self):
    	return self.nRecords

    def getMainNameForTerm(self, term):
    	if(term not in self.allTerms.values()):
    		return None
    	return termToMainNameMap.get(term)

    def getMainNameForId(self, id):
    	if(id not in self.idToMainNameMap):
    		return None
    	return idToMainNameMap.get(id)

    def getSynonyms(self, term):
        mainName = getMainNameForTerm(term)
        if(term not in self.synonymMap):
            return None
        return synonymMap.get(term)


    #double check this one not sure if handling null's conversion from java code right
    def getId(self, term):
        if (containsTermLowerCase(term) == None):
            return None
        mainName = termToMainNameMap.get(term.lower())
        return termToIdMap.get(mainName)

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

'''


    abstract void readFromInputStream(InputStream inputStream);
}
'''
