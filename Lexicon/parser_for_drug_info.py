import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.corpus import stopwords
import re

strucs = []


def cleanIndication(indication):
	indication =indication.lower() 
	indications = indication.split("treatment of ")
	if(len(indications) > 1):
		indications = indications[1].split(", ")
		return "|".join(indications)
	else:
		return indication

def sentenceStruct(indication):
	tokens = nltk.word_tokenize(indication)
	tagged = nltk.pos_tag(tokens)

	try:
		strucs.append([(tag) for word, tag in tagged])
	except:
		pass

def nlp(indication):

	tokens = nltk.word_tokenize(indication)

	lemmatizer = WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]

	tagged = nltk.pos_tag(tokens)

	#s=set(stopwords.words('english'))
	#print(lambda w: not w in s,indication.split())
	

	#corpus_root = "NCBI_corpus_training.txt"
	#wordlists = PlaintextCorpusReader(corpus_root, '.*')


	grammar = "NP: {<NN><IN><JJ>?<NN>|<NNP>*<JJ>?}" 
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(tagged) 
	try:
		result = [t for t in result if t[1] == "NP"]
	except:
		result = None

	#indication =indication.lower() 
	
	#s = set(stopwords.words('english'))
	#tokens = [token for token in tokens if token not in s]

	#tagged = nltk.pos_tag(tokens)
	#return tagged
	lemmatizer = WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	#s = set(stopwords.words('english'))
	#tokens = [token for token in tokens if token not in s]
	#print(tokens)
	#tagged = nltk.pos_tag(tokens)
	#rd_parser = nltk.RecursiveDescentParser(grammar)
	#for tree in rd_parser.parse(tokens):
	#	print(tree)
	return result



	#for token in tokens:
	#		print(token)
	#		print(wn.synset(token).min_depth())
	#		print(token)
	#tagged = nltk.pos_tag(tokens)
	#for tag in tagged:
	#	if(tag[1] == "NN"):
	#		print(tag[0])
	#parser = nltk.ChartParser(

	#print(tagged)

	#return result

d = {}

name = ""
status = ""
indication = ""
with open('../../full database.xml', 'r' , encoding='utf-8') as f:
    for line in f:
    	if((len(line) > 10) & (line[2:8] == "<name>")):
    		name = line[8:-8]
    		status = ""
    		indication = ""
    	if((len(line) > 25) & (line[4:27] == "<group>approved</group>")):
    		status = "approved"
    	if((len(line) > 30) & (line[2:14] == "<indication>")):
    		indication = line[14:-15].split('.')
    		if((status == "approved") & (name != "")):
    			d[name] = indication[0]

f = open('drugs_usage_r.tsv', 'w', encoding='utf-8')
f.write("drug\tusage\n")
for key in d:
	f.write("%s\t%s\n" %(key, d[key]))
f.close()

for struc in strucs:
	print(struc)

   