import hashlib
import requests


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


sequence = 'CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'
md5 = calculate_md5(sequence)
print(rnacentral_id(md5))
