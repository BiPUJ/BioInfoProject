import unittest
from Modules.PDBe_module import *


class PDBeTest(unittest.TestCase):
    def test_get_summary_info(self):
        self.assertTrue(get_summary_info('2ce3'))
        self.assertTrue(get_summary_info('2CE3'))
        self.assertIsNone(get_summary_info('asdasdasd'))
        self.assertIsNone(get_summary_info('2'))
        self.assertIsNone(get_summary_info(''))

    def test_get_molecules(self):
        self.assertTrue(get_molecules('2ce3'))
        self.assertTrue(get_molecules('2CE3'))
        self.assertIsNone(get_molecules('asdasdasd'))
        self.assertIsNone(get_molecules('2'))
        self.assertIsNone(get_molecules(''))

    def test_get_publications(self):
        self.assertTrue(get_publications('2ce3'))
        self.assertTrue(get_publications('2CE3'))
        self.assertIsNone(get_publications('asdasdasd'))
        self.assertIsNone(get_publications('2'))
        self.assertIsNone(get_publications(''))

    def test_get_experiment(self):
        self.assertTrue(get_experiment('2ce3'))
        self.assertTrue(get_experiment('2CE3'))
        self.assertIsNone(get_experiment('asdasdasd'))
        self.assertIsNone(get_experiment('2'))
        self.assertIsNone(get_experiment(''))

    def test_get_NMR_resource(self):
        self.assertTrue(get_NMR_resource('2k8v'))
        self.assertTrue(get_NMR_resource('2k7v'))
        self.assertIsNone(get_NMR_resource('asdasdasd'))
        self.assertIsNone(get_NMR_resource('2'))
        self.assertIsNone(get_NMR_resource(''))

    def test_get_ligands(self):
        self.assertTrue(get_ligands('1cbs'))
        self.assertIsNone(get_ligands('asdasdasd'))
        self.assertIsNone(get_ligands('2'))
        self.assertIsNone(get_ligands(''))

    def test_get_modified_residues(self):
        self.assertTrue(get_modified_residues('4v5j'))
        self.assertTrue(get_modified_residues('4V5J'))
        self.assertIsNone(get_modified_residues('asdasdasd'))
        self.assertIsNone(get_modified_residues('2'))
        self.assertIsNone(get_modified_residues(''))

    def test_get_mutated_residues(self):
        self.assertTrue(get_mutated_residues('4v5j'))
        self.assertTrue(get_mutated_residues('4V5J'))
        self.assertIsNone(get_mutated_residues('asdasdasd'))
        self.assertIsNone(get_mutated_residues('2'))
        self.assertIsNone(get_mutated_residues(''))

    def test_get_release_status(self):
        self.assertTrue(get_release_status('1cbs'))
        self.assertTrue(get_release_status('1CBS'))
        self.assertIsNone(get_release_status('asdasdasd'))
        self.assertIsNone(get_release_status('2'))
        self.assertIsNone(get_release_status(''))

    def test_get_observed_ranges(self):
        self.assertTrue(get_observed_ranges('1cbs'))
        self.assertTrue(get_observed_ranges('1CBS'))
        self.assertIsNone(get_observed_ranges('asdasdasd'))
        self.assertIsNone(get_observed_ranges('2'))
        self.assertIsNone(get_observed_ranges(''))

    def test_get_observed_ranges_in_PDB_chain(self):
        self.assertTrue(get_observed_ranges_in_PDB_chain('1cbs', 'A'))
        self.assertTrue(get_observed_ranges_in_PDB_chain('1CBS', 'A'))
        self.assertIsNone(get_observed_ranges_in_PDB_chain('asdasdasd', 'asdadas'))
        self.assertIsNone(get_observed_ranges_in_PDB_chain('2', '222'))
        self.assertIsNone(get_observed_ranges_in_PDB_chain('', ''))

    def test_get_secondary_structure(self):
        self.assertTrue(get_secondary_structure('1cbs'))
        self.assertTrue(get_secondary_structure('1CBS'))
        self.assertIsNone(get_secondary_structure('asdasdasd'))
        self.assertIsNone(get_secondary_structure('2'))
        self.assertIsNone(get_secondary_structure(''))

    def test_get_list_of_residues_with_modelling_information(self):
        self.assertTrue(get_list_of_residues_with_modelling_information('1cbs'))
        self.assertTrue(get_list_of_residues_with_modelling_information('1CBS'))
        self.assertIsNone(get_list_of_residues_with_modelling_information('asdasdasd'))
        self.assertIsNone(get_list_of_residues_with_modelling_information('2'))
        self.assertIsNone(get_list_of_residues_with_modelling_information(''))

    def test_get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain(self):
        self.assertTrue(get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('1cbs', 'A'))
        self.assertTrue(get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('1CBS', 'A'))
        self.assertIsNone(
            get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('asdasdasd', 'asdadas'))
        self.assertIsNone(get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('2', '222'))
        self.assertIsNone(get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('', ''))

    def test_get_binding_sites(self):
        self.assertTrue(get_binding_sites('1cbs'))
        self.assertTrue(get_binding_sites('1CBS'))
        self.assertIsNone(get_binding_sites('asdasdasd'))
        self.assertIsNone(get_binding_sites('2'))
        self.assertIsNone(get_binding_sites(''))

    def test_get_URLs_of_various_files_associated_with_a_PDB_entry(self):
        self.assertTrue(get_URLs_of_various_files_associated_with_a_PDB_entry('1cbs'))
        self.assertTrue(get_URLs_of_various_files_associated_with_a_PDB_entry('1CBS'))
        self.assertIsNone(get_URLs_of_various_files_associated_with_a_PDB_entry('asdasdasd'))
        self.assertIsNone(get_URLs_of_various_files_associated_with_a_PDB_entry('2'))
        self.assertIsNone(get_URLs_of_various_files_associated_with_a_PDB_entry(''))

    def test_get_ratio_of_observed_residues(self):
        self.assertTrue(get_ratio_of_observed_residues('1cbs'))
        self.assertTrue(get_ratio_of_observed_residues('1CBS'))
        self.assertIsNone(get_ratio_of_observed_residues('asdasdasd'))
        self.assertIsNone(get_ratio_of_observed_residues('2'))
        self.assertIsNone(get_ratio_of_observed_residues(''))


if __name__ == '__main__':
    unittest.main()
