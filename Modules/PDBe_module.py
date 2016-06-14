import urllib.request
import json
import tkinter as tk
from tkinter import filedialog


def get_summary_info(id, save='false', isShowed='false'):
    """"
    This call provides a summary of properties of a PDB entry,
    such as the title of the entry, list of depositors,
    date of deposition, date of release, date of latest revision,
    experimental method, list of related entries in case split entries, etc.

    :param id:  String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:entry_authors, number_of_entities, title, processing_site, deposition_date, split_entry, revision_date,
    assemblies, experimental_method, related_structures, deposition_site, release_date, experimental_method_class
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_molecules(id, save='false', isShowed='false'):
    """
    This call provides the details of molecules (or entities in mmcif-speak) modelled in the entry, such as entity id,
    description, type, polymer-type (if applicable), number of copies in the entry,
    sample preparation method, source organism(s) (if applicable), etc.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:molecule_name, chem_comp_ids,molecule_type, in_chains, number_of_copies, ca_p_only, in_struct_asyms,mutation_flag,entity_id,
    weight,sample_preparation,gene_name, molecule_type, sequence, source, entity_id, weight, synonym, number_of_copies, length, in_struct_asyms,
    sample_preparation,pdb_sequence_indices_with_multiple_residues, pdb_sequence, chem_comp_ids
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_publications(id, save='false', isShowed='false'):
    """
    This call provides details of publications associated with an entry,
    such as title of the article, journal name,
    year of publication, volume, pages, doi, pubmed_id, etc.
    Primary citation is listed first.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return: pubmed_id, publication, authors, pub_id, title, doi, pubmed_id, type, journal_info, pages, issue, year,
    volume, pdb_abbreviation, ISO_abbreviation, abstract, author_list
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/publications/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_experiment(id, save='false', isShowed='false'):
    """
    This call provides details of experiment(s) carried out in determining the structure of the entry.
    Each experiment is described in a separate dictionary.
    For X-ray diffraction, the description consists of resolution,
    spacegroup, cell dimensions, R and Rfree, refinement program, etc.
    For NMR, details of spectrometer, sample, spectra, refinement, etc. are included.
    For EM, details of specimen, imaging, acquisition, reconstruction, fitting etc. are included.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return: experimental_method_class, resolution, r_factor, spacegroup, starting_model, refinement_software,
    phasing_method, r_free, structure_determination_method, resolution_low, r_free_selection_details,r_free_percent_reflections,
    expression_host_scientific_name, resolution_high, diffraction_experiment, experiment_data_available, num_reflections,
    experimental_method, percent_reflections_observed, cell, completeness, crystal_growth, r_work
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/experiment/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_NMR_resource(id, save='false', isShowed='false'):
    """
    This call provides URLs of available additional resources for NMR entries.
    E.g., mapping between structure (PDB) and chemical shift (BMRB) entries.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return: vivaldi_link_restraints, vivaldi_link_olderado, casd_nmr_link, uniquely_linked_bmrb_entries,
    vivaldi_link_default, vivaldi_link_score, vivaldi_link_vasco, related_bmrb_entries, olderado_link,
    nrg_link
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/nmr_resources/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_ligands(id, save='false', isShowed='false'):
    """
    This call provides a a list of modelled instances of ligands,
    i.e. 'bound' molecules that are not waters.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:entity_id, author_residue_number, chem_comp_id, residue_number,
    alternate_conformers, chem_comp_name, chain_id, struct_asym_id, author_insertion_code
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/ligand_monomers/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_modified_residues(id, save='false', isShowed='false'):
    """
    This call provides a list of modelled instances of modified amino acids or nucleotides in protein,
    DNA or RNA chains.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:entity_id, author_residue_number, chem_comp_id, residue_number,
    alternate_conformers, chem_comp_name, chain_id, struct_asym_id, author_insertion_code
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/modified_AA_or_NA/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_mutated_residues(id, save='false', isShowed='false'):
    """
    This call provides a list of modelled instances of mutated amino acids in proteins in an entry.
    (Note that at present it does not provide information about mutated nucleotides in RNA or DNA chains,
    but it would do so in near future.)

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:entity_id, author_residue_number, chem_comp_id, residue_number,
    chem_comp_name, chain_id, struct_asym_id, author_insertion_code,
    mutation_details
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/mutated_AA_or_NA/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_release_status(id, save='false', isShowed='false'):
    """
    This call provides status of a PDB entry (released, obsoleted, on-hold etc)
    along with some other information such as authors, title, experimental method, etc.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:experimental_method, since, obsoletes, superceded_by, entry_authors,experimental_method_class,
    status_code, title
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/status/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_observed_ranges(id, save='false', isShowed='false'):
    """
    This call provides observed ranges,
    i.e. segments of structural coverage,
    of polymeric molecules that are modelled fully or partly.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_observed_ranges_in_PDB_chain(id, chain, save='false', isShowed='false'):
    """
    This call provides observed ranges,
    i.e. segments of structural coverage,
    of polymeric molecules in a particular chain.

    :param id: String - 4-character PDB id code.
    :param chain: String - PDB chain id.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/' + format(id) + '/chain/' + format(chain)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_secondary_structure(id, save='false', isShowed='false'):
    """
    This call provides details about residue ranges of regular secondary structure (alpha helices and beta strands)
    found in protein chains of the entry.
    For strands, sheet id can be used to identify a beta sheet.

    :param id: String - 4 -character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code,
    strands, helices, sheet_id
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/secondary_structure/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_list_of_residues_with_modelling_information(id, save='false', isShowed='false'):
    """
    This call lists all residues (modelled or otherwise) in the entry, except waters,
    along with details of the fraction of expected atoms modelled for the residue and any alternate conformers.

    :param id: String - 4 -character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code,
    observed_ratio
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/residue_listing/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain(id, chain, save='false',
                                                                               isShowed='false'):
    """
    This call lists all residues (modelled or otherwise) in the entry,
    except waters, along with details of the fraction of expected atoms modelled for the residue and any alternate conformers.

    :param id: String - 4-character PDB id code.
    :param chain: String - PDB chain id.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code,
    chain_id, entity_id
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/' + format(id) + '/chain/' + format(chain)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_binding_sites(id, save='false', isShowed='false'):
    """
    This call provides details on binding sites in the entry as per
    STRUCT_SITE records in PDB files (or mmcif equivalent thereof),
    such as ligand, residues in the site, description of the site, etc.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, author_residue_number, residue_number, author_insertion_code,
    chain_id, entity_id, evidence_code, details, site_id, site_residues, symmetry_symbol
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/binding_sites/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_URLs_of_various_files_associated_with_a_PDB_entry(id, save='false', isShowed='false'):
    """
    This call provides URLs and brief descriptions (labels) for PDB and mmcif files, biological assembly files,
    FASTA file for sequences, SIFTS cross reference XML files, validation XML files, X-ray structure factor file,
    NMR experimental constraints files, etc. Please note that these files are also available on https.

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:label, url, downloads, views, SIFTS, assembly
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/files/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_ratio_of_observed_residues(id, save='false', isShowed='false'):
    """
    This call provides the ratio of observed residues for each chain in each molecule (or entity in mmcif-speak) of a pdb entry.
    The list of chains within an entity is sorted by observed_ratio (descending order),
    partial_ratio (ascending order),
    and number_residues (descending order).

    :param id: String - 4-character PDB id code.
    :param save:  Boolean - 'true' if you want to save output to file, 'false'(default) not saving output
    :param isShowed: Boolean - 'true' if you want to show output in console, 'false'(default) not showing output
    :return:struct_asym_id, number_residues, chain_id,
    observed_ratio
    """
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/observed_residues_ratio/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        toShow = json.dumps(result, indent=2)
        if (isShowed == 'true'):
            print(toShow)
        if (save == 'true'):
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename()
            if file_path:
                file = open(file_path + '.txt', 'w')
                file.write(toShow)
                file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')
