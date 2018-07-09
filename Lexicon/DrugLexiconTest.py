
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
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertTrue(drugs.containsTermLowerCase("1,7-dimethylxanthine"))
        self.assertTrue(drugs.containsTermLowerCase("paraxanthine"))
        self.assertTrue(drugs.containsTermLowerCase("MEDR-640"))
        self.assertTrue(drugs.containsTermLowerCase("Adinazolamum [INN-Latin]"))
        self.assertTrue(drugs.containsTermLowerCase("T-cell growth factor"))
        self.assertTrue(drugs.containsTermLowerCase("Proleukin"))
        self.assertTrue(drugs.containsTermLowerCase("Aldose reductase inhibitors"))
        self.assertFalse(drugs.containsTermLowerCase(""))

    def testGetAllMainTerms(self):
        #appears to be working need to figure out unit testing for dict values
        pass

    def testGetnRecords(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(drugs.getnRecords(), 99)

    def testGetMainNameForTerm(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(drugs.getMainNameForTerm("p-HPPH glucuronide"), "5-phenyl-5-(4-hydroxyphenyl)hydantoin glucuronide")


    def testGetMainNameForId(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(drugs.getMainNameForId("PA134967247"), "2-methoxyestradiol")

    def testGetSynonyms(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(drugs.getSynonyms("p-HPPH glucuronide"), ['5-phenyl-5-(4-hydroxyphenyl)hydantoin glucuronide', 'hydroxyphenytoin glucuronide', 'p-HPPH glucuronide'])

    def testGetId(self):
        drugs = DrugLexicon()
        drugs.readFromInputStream('drug-lexicon-sample.tsv')
        self.assertEqual(drugs.getId("ReoPro"), "PA448006")

if __name__ == '__main__':
    unittest.main(verbosity=2)
