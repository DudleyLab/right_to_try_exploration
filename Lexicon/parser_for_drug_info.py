
from bs4 import BeautifulSoup

import re

d = {}

name = ""
status = ""
indication = ""
with open('full database.xml', 'r' , encoding='utf-8') as f:
    for line in f:
    	if((len(line) > 10) & (line[2:8] == "<name>")):
    		name = line[8:-8]
    		status = ""
    		indication = ""
    	if((len(line) > 25) & (line[4:27] == "<group>approved</group>")):
    		status = "approved"
    	if((len(line) > 30) & (line[2:14] == "<indication>")):
    		indication = line[14:-15]
    		if((status == "approved") & (name != "")):
    			d[name] = indication

f = open('drugs_usage_r.tsv', 'w', encoding='utf-8')
f.write("drug\tusage\n")
for key in d:
	f.write("%s\t%s\n" %(key, d[key]))
f.close()

    		