import urllib.request
import xmltodict


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
    return out


'''print(get_info("2B4W"))'''


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


pdb_file = get_pdb_file('4zps', filetype='pdb', compression=False)
print(pdb_file[:1000])
