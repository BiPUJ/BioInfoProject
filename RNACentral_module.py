import hashlib
import requests
import urllib.request
import json


def calculate_md5(seq):
    seq = seq.replace('U', 'T')
    m = hashlib.md5()
    m.update(seq.encode("unicode_escape"))
    return m.hexdigest()


def rnacentral_id(md5):
    url = 'http://rnacentral.org/api/v1/rna'
    temp = requests.get(url, params={'md5': md5})
    data = temp.json()
    if data['count'] > 0:
        return data['results'][0]['rnacentral_id']
    else:
        return 'iD not found'


def information_RNACentral(id):
    path_url = 'http://rnacentral.org/api/v1/rna/'
    url = path_url + id
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        return result
    except:
        print('Invalid Input')


def publications_RNACentral(id):
    path_url = 'http://rnacentral.org/api/v1/rna/' + id + '/publications'
    print(path_url)
    url = path_url
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        return result
    except:
        print('Invalid Input')


def xrefs_RNACentral(id):
    path_url = 'http://rnacentral.org/api/v1/rna/' + id + '/xrefs'
    print(path_url)
    url = path_url
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        file = open(id + '-xrefs_RNACentral.txt', 'w')
        file.write(result)
        file.close
        return result
    except:
        print('Invalid Input')


sequence = 'CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'
md5 = calculate_md5(sequence)
# print(rnacentral_id(md5))
# print(information_RNACentral('URS0000000001'))
# print(publications_RNACentral('URS0000000001'))
print(xrefs_RNACentral('URS0000000001'))
