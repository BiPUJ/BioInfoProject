import hashlib
import requests


def get_md5(sequence):
    """
    Calculate md5 for an RNA sequence
    """
    # RNAcentral stores DNA md5 hashes
    sequence = sequence.replace('U', 'T')
    # get the md5 digest
    m = hashlib.md5()
    m.update(sequence.encode("utf8"))
    return m.hexdigest()


# get the RNAcentral id
def get_rnacentral_id(md5):
    """
    Parse json output and return the RNAcentral id.
    """
    url = 'http://rnacentral.org/api/v1/rna'
    r = requests.get(url, params={'md5': md5})
    data = r.json()
    if data['count'] > 0:
        return data['results'][0]['rnacentral_id']
    else:
        return 'RNAcentral id not found'


# This sequence has an RNAcentral id
sequence = 'CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'
md5 = get_md5(sequence)
print(get_rnacentral_id(md5))  # URS00002C9E9D
