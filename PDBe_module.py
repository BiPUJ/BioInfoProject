import urllib.request
import json
import tkinter as tk
from tkinter import filedialog


def get_summary_info(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_molecules(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_publications(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/publications/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_related_publication(id):  # nie dziala zapytanie
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/related_publications/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_experiment(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/experiment/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_NMR_resource(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/nmr_resources/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_ligands(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/ligand_monomers/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_modified_residues(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/modified_AA_or_NA/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_mutated_residues(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/mutated_AA_or_NA/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_release_status(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/status/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_observed_ranges(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_observed_ranges_in_PDB_chain(id, chain):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/' + format(id) + '/chain/' + format(chain)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_secondary_structure(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/secondary_structure/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_list_of_residues_with_modelling_information(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/residue_listing/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain(id, chain):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/' + format(id) + '/chain/' + format(chain)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_binding_sites(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/binding_sites/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_URLs_of_various_files_associated_with_a_PDB_entry(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/files/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')


def get_ratio_of_observed_residues(id):
    path_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/observed_residues_ratio/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('ID not found')
        else:
            print('Invalid Input')

# print(get_summary_info('2asc'))
# print(get_molecules('1cbs'))
# print(get_publications('1cbs'))
#  print(get_related_publication('1cbs'))
# print(get_experiment('1cbs'))
# print(get_experiment('2k8v'))
#  print(get_ligands('1cbs'))
# print(get_modified_residues('4v5j'))
# print(get_mutated_residues('4v5j'))
# print(get_release_status('1cbs'))
# print(get_observed_ranges('1cbs'))
# print(get_observed_ranges_in_PDB_chain('1cbs','A'))
# print(get_secondary_structure('1cbs'))
# print(get_list_of_residues_with_modelling_information('1cbs'))
# print(get_list_of_residues_with_modelling_information_for_a_particular_PDB_chain('1cbs','A'))
# print(get_binding_sites('1cbs'))
# print(get_URLs_of_various_files_associated_with_a_PDB_entry('1cbs'))
# print(get_ratio_of_observed_residues('2k8v'))
