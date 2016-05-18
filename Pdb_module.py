import urllib.request
import xmltodict
from json import loads, dumps
from collections import OrderedDict, Counter
from itertools import repeat, chain
import urllib.request
import time
import re
from json import loads, dumps
import warnings


def get_info(pdb_id, url_root='http://www.rcsb.org/pdb/rest/describeMol?structureId='):
    '''
        Input:
        pdb_id : string
        A 4 character string giving a pdb entry
        Output:
        OrderedDict:
        structureId,
        length,
        type etc
    '''
    url = url_root + pdb_id
    req = urllib.request.Request(url)
    temp = urllib.request.urlopen(req)
    result = temp.read()
    assert result
    out = xmltodict.parse(result, process_namespaces=True)
    for k, v in out.items():
        print(k, '-', v)
    return out


# get_info("2B4W")


def get_pdb_file(pdb_id, filetype='pdb', compression=False):
    '''
    Input:
    pdb_id - string a 4 character giving a pdb entry
    filetype - string
    capabilities:
    - pdb
    - cif
    - xml
    compression - bool retrieve compressed (gz) version of the file
    '''
    if (len(pdb_id) == 4 and (compression == True or compression == False) and
            (filetype == 'pdb' or filetype == 'cif' or filetype == 'xml')):
        url = 'http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat='
        url += filetype
        if compression:
            url += '&compression=YES'
        else:
            url += '&compression=NO'
        url += '&structureId=' + pdb_id
        req = urllib.request.Request(url)
        f = urllib.request.urlopen(req)
        result = f.read()
        result = result.decode('unicode_escape')
        return result
    else:
        print('invalid input')


# pdb_file = get_pdb_file('4zps', filetype='pdb', compression=False)
# print(pdb_file[:1000])

def describe_pdb(pdb_id):
    '''
    Description and metadata of a PDB  entry
    Input:
    pdb_id: string - 4 character
    Out: description from PDB
    '''
    out = get_info(pdb_id, url_root='http://www.rcsb.org/pdb/rest/describePDB?structureId=')
    out = to_dict(out)
    out = remove_at_sign(out['PDBdescription']['PDB'])
    for k, v in out.items():
        print(k, '-', v)
    return out


def to_dict(odict):
    '''
    Converter to dictionary
    convert to key: val pairs
    '''
    out = loads(dumps(odict))
    return out


def remove_at_sign(temp):
    '''
    Remove the "@" character from the beginning of key names in a dict()
    '''
    tagged_keys = [thing for thing in temp.keys() if thing.startswith('@')]
    for tag_key in tagged_keys:
        temp[tag_key[1:]] = temp.pop(tag_key)

    return temp


# describe_pdb('4lza')

def get_raw_blast(pdb_id, output_form='HTML', chain_id='A'):
    '''
    Download full blast structure
    Input: pdb_id , chain_id, output format
    Output: entire blast
    '''
    url_root = 'http://www.rcsb.org/pdb/rest/getBlastPDB2?structureId='
    url = url_root + pdb_id + '&chainId=' + chain_id + '&outputFormat=' + output_form
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    result = f.read()
    result = result.decode('unicode_escape')
    assert result

    return result


print(get_raw_blast('2a1o', output_form='HTML', chain_id='A'))
