import urllib.request
import xmltodict
from bs4 import BeautifulSoup
import xml.etree.ElementTree
from json import loads, dumps
from collections import OrderedDict, Counter
from itertools import repeat, chain
import urllib.request
import time
import re
import json
from json import loads, dumps
import warnings


def information(id, path_url='http://www.rcsb.org/pdb/rest/describeMol?structureId='):
    url = path_url + id
    request = urllib.request.Request(url)
    temp = urllib.request.urlopen(request)
    result = temp.read()
    assert result
    out = xmltodict.parse(result, process_namespaces=True)
    return out


def show_information(id):
    out = information(id, path_url='http://www.rcsb.org/pdb/rest/describeMol?structureId=')
    out = json.dumps(out, indent=4)
    return out


def file_pdb(id, filetype='pdb', compression=False):
    if (len(id) == 4 and (compression == True or compression == False) and
            (filetype == 'pdb' or filetype == 'cif' or filetype == 'xml')):
        path_url = 'http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat='
        path_url += filetype
        if compression:
            path_url += '&compression=YES'
        else:
            path_url += '&compression=NO'
            path_url += '&structureId=' + id
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        file = open(id + '-pdb_file.txt', 'w')
        file.write(result)
        file.close
        return result
    else:
        print('invalid input')


def pdb_describtion_metadata(id):
    if (len(id) == 4):
        out = information(id, path_url='http://www.rcsb.org/pdb/rest/describePDB?structureId=')
        out = remove_sign(out['PDBdescription']['PDB'])
        out = json.dumps(out, indent=4)
        return out
    else:
        print('Invalid input')


def remove_sign(temp):
    keys = [thing for thing in temp.keys() if thing.startswith('@')]
    for tag_key in keys:
        temp[tag_key[1:]] = temp.pop(tag_key)
    return temp


def raw_blast_file(id, chain='A'):
    url_path = 'http://www.rcsb.org/pdb/rest/getBlastPDB2?structureId='
    url = url_path + id + '&chainId=' + chain + '&outputFormat=' + 'HTML'
    request = urllib.request.Request(url)
    f = urllib.request.urlopen(request)
    result = f.read()
    result = result.decode('unicode_escape')
    soup = BeautifulSoup(result, "html.parser")
    out = soup.get_text()
    assert result
    file = open(id + '-blast_file.txt', 'w')
    file.write(out)
    file.close
    return out


def chemical_description(id):
    out = information(id, path_url='http://www.rcsb.org/pdb/rest/describeHet?chemicalID=')
    out = json.dumps(out, indent=4)
    return out


def ligands_description(id):
    if (len(id) > 3):
        out = information(id, path_url='http://www.rcsb.org/pdb/rest/ligandInfo?structureId=')
        out = json.dumps(out, indent=4)
        return out
    else:
        print('Invalid input')

# print(ligands_description('1cbe'))
# print(chemical_description('a3c'))
# print(pdb_describtion_metadata('4cla'))
# file_pdb('4zpo', filetype='pdb', compression=False)
# print(show_information("2CA4"))
# raw_blast_file('2csko', chain='A')
