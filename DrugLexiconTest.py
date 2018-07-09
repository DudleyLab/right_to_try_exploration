
#re-reading the drug-lexicon for every test very innefficent
#need to figure out way to initilize variable for unit test in python
from DrugLexicon import Lexicon, DrugLexicon
import unittest

class testLexicon(unittest.TestCase):

    def testNumberOfEntries(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(len(drugs.getAllTerms()), 588)


    def testContainsTerm(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertTrue(drugs.containsTerm("1,7-dimethylxanthine"))
        self.assertTrue(drugs.containsTerm("paraxanthine"))
        self.assertTrue(drugs.containsTerm("MEDR-640"))
        self.assertTrue(drugs.containsTerm("Adinazolamum [INN-Latin]"))
        self.assertTrue(drugs.containsTerm("T-cell growth factor"))
        self.assertTrue(drugs.containsTerm("Proleukin"))
        self.assertTrue(drugs.containsTerm("Aldose reductase inhibitors"))
        self.assertFalse(drugs.containsTerm(""))

    def testContainsTermLowerCase(self):
        pass

    def testGetAllMainTerms(self):
        pass

    def testGetnRecords(self):
        pass

    def testGetMainNameForTerm(self):
        pass

    def testGetMainNameForId(self):
        pass

    def testGetSynonyms(self):
        pass

    def testGetId(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
