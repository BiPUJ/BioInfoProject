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


print(get_info("2B4W"))
