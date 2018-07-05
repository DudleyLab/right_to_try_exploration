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
        return term in self.allTerms

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
    	if(term not in self.allTerms):
    		return None
    	return termToMainNameMap.get(term)

    def getMainNameForId(self, id):
    	if(id not in self.idToMainNameMap):
    		return None
    	return idToMainNameMap.get(id)


    def gill(self):
     	print("hi")

x = Lexicon()
print(x.containsTermLowerCase('HI'))

'''
  public String getId(String term) {
        if (!containsTermLowerCase(term)) {
            return null;
        }
        String mainName = termToMainNameMap.getOrDefault(term.toLowerCase(Locale.US), null);
        return termToIdMap.getOrDefault(mainName, null);
    }

    public List<String> getParents(String myId) {
        if (!parentMap.containsKey(myId)) {
            return new ArrayList<>();
        }
        List<String> parentIds = parentMap.get(myId);
        List<String> parents = new ArrayList<>();
        parents.addAll(parentIds);
        for (String parentId : parentIds) {
            parents.addAll(getParents(parentId));
        }
        return parents;
    }

    public List<String> getAncestors(String name) {
        String id = getId(name);
        if (id == null) {
            return null;
        }
        return getParents(id);
    }

    public Set<String> getSynonyms(String term) {
        String mainName = getMainNameForTerm(term);
        if (!synonymMap.containsKey(mainName)) {  // if this term is not a main term, it won't be in the synonym map
            return null;
        }
        return synonymMap.get(mainName);
    }

    public Set<String> getSynonymsLowercaseConcatenated(String term) {
        String mainName = getMainNameForTerm(term);
        if (!synonymMap.containsKey(mainName)) {  // if this term is not a main term, it won't be in the synonym map
            return null;
        }
        Set<String> formattedSynonyms = synonymMap.get(mainName).stream().map(
                synonym -> synonym.toLowerCase().replace(' ', '_')).collect(Collectors.toSet());
        return formattedSynonyms;
    }

    abstract void readFromInputStream(InputStream inputStream);
}
'''
