import unittest
from Modules.RNACentral_module import *


class PDBeTest(unittest.TestCase):
    def test_calculate_md5(self):
        self.assertTrue(calculate_md5('CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'))
        self.assertTrue(calculate_md5('asdasdasd'))
        self.assertTrue(calculate_md5('2'))
        self.assertTrue(calculate_md5(''))

    def test_rnacentral_id(self):
        self.assertTrue(rnacentral_id('2ca3va2dfa53sda'))
        self.assertTrue(rnacentral_id('asdasdasd'))
        self.assertTrue(rnacentral_id('2'))

    def test_information_RNACentral(self):
        self.assertTrue(information_RNACentral('URS0000000001'))
        self.assertTrue(information_RNACentral('URS0000000011'))
        self.assertIsNone(information_RNACentral('asdasdasd'))
        self.assertIsNone(information_RNACentral('2'))

    def test_publications_RNACentral(self):
        self.assertTrue(publications_RNACentral('URS0000000001'))
        self.assertTrue(publications_RNACentral('URS0000000011'))
        self.assertIsNone(publications_RNACentral('asdasdasd'))
        self.assertIsNone(publications_RNACentral('2'))
        self.assertIsNone(publications_RNACentral(''))

    def test_xrefs_RNACentral(self):
        self.assertTrue(xrefs_RNACentral('URS0000000001'))
        self.assertTrue(xrefs_RNACentral('URS0000000011'))
        self.assertIsNone(xrefs_RNACentral('asdasdasd'))
        self.assertIsNone(xrefs_RNACentral('2'))
        self.assertIsNone(xrefs_RNACentral(''))

    def test_filter_length(self):
        self.assertTrue(filter_length(200))
        self.assertTrue(filter_length(200, 3, 50))
        self.assertTrue(filter_length(2))
        self.assertIsNone(filter_length(2, -2))
        self.assertIsNone(filter_length(2, 2, -2))

    def test_filter_min_length(self):
        self.assertTrue(filter_min_length(200))
        self.assertTrue(filter_min_length(200, 3, 50))
        self.assertTrue(filter_min_length(2))
        self.assertIsNone(filter_min_length(2, -2))

    def test_filter_max_length(self):
        self.assertTrue(filter_max_length(200))
        self.assertTrue(filter_max_length(200, 3, 50))
        self.assertTrue(filter_max_length(2))
        self.assertIsNone(filter_max_length(2, -2))

    def test_filter_min_max_length(self):
        self.assertTrue(filter_min_max_length(200, 300))
        self.assertTrue(filter_min_max_length(200, 300, 2, 7))
        self.assertTrue(filter_min_max_length(2, 3))

    def test_filter_by_database(self):
        self.assertTrue(filter_by_database('srpdb', 2, 7))
        self.assertTrue(filter_by_database('srpdb', 3, 50))
        self.assertTrue(filter_by_database('srpdb'))
        self.assertIsNone(filter_by_database(2, -2))

    def test_filter_by_external_id(self):
        self.assertTrue(filter_by_external_id('MIMAT0000091'))
        self.assertTrue(filter_by_external_id('MIMAT0010091'))

    def test_filter_database_min_length(self):
        self.assertTrue(filter_database_min_length('srpdb', 2, 7))
        self.assertTrue(filter_database_min_length('srpdb', 3, 50))
        self.assertTrue(filter_database_min_length('srpdb', 2))

    def test_filter_database_max_length(self):
        self.assertTrue(filter_database_max_length('srpdb', 200, 7))
        self.assertTrue(filter_database_max_length('srpdb', 2))


if __name__ == '__main__':
    unittest.main()
