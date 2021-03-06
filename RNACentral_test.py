import hashlib
import requests
import urllib.request
import json

def calculate_md5(seq):
    """
    Calculate md5 for an RNA sequence
    """
    # RNAcentral stores DNA md5 hashes
    seq = seq.replace('U', 'T')
    # get the md5 digest
    m = hashlib.md5()
    m.update(seq.encode("unicode_escape"))
    return m.hexdigest()

# get the RNAcentral id
def rnacentral_id(md5):
    """
    Parse json output and return the RNAcentral id.
    """
    url = 'http://rnacentral.org/api/v1/rna'
    temp = requests.get(url, params={'md5': md5})
    data = temp.json()
    if data['count'] > 0:
        return data['results'][0]['rnacentral_id']
    else:
        return 'iD not found'

def information_RNACentral(id):
    """"
        This call provides a summary of properties of a RNACentral entry,
        such as the title of the entry, number of entities,
        date of deposition, revision date, release date,
        experimental method, list of related entries in case split entries, etc.

        :param id:  String - 4-character RNACentral id code.
        :return:publications, xrefs, length, rnacentral_id, url, sequence, md5
    """
    path_url = 'http://rnacentral.org/api/v1/rna/'
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except:
        print('Invalid Input')

def publications_RNACentral(id):
    """
        This call provides details of publications associated with an entry,
        such as title of the article, journal name,
        year of publication, count, doi, pubmed_id, etc.
        Primary citation is listed first.

        :param id: String - 4-character PDB id code.
        :return: next, previous, count, pubmed_id, publication, authors, pub_id, title, doi, pubmed_id
    """
    path_url = 'http://rnacentral.org/api/v1/rna/' + format(id) + '/publications'
    url = path_url
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except:
        print('Invalid Input')

def xrefs_RNACentral(id):
    """
    List of cross-references for a particular RNA sequence such as
    database, if is active,  first seen last seen etc

    :param id: String - 4-character PDB id code.
    :return: first_seen,last_seen,database,is_expert_db,taxid,is_active,
    accession: product, source_url, description, species, rna_type, id, expert_db_url,
    optional_id, url, citations, external_id, organelle, gene
    """
    path_url = 'http://rnacentral.org/api/v1/rna/' + format(id) + '/xrefs'
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except:
        print('Invalid Input')

def filter_length(len, page=1, pageSize=10):
    """
    This call returns list of structures which have length equal len param.

    :param len: Number - structure length
    :param page: Number - specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?length='
    url = path_url + format(len) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_min_length(len, page=1, pageSize=10):
    """
    This call returns list of structures which have length equal or bigger than len param.

    :param len: Number - specifies the minimum length
    :param page: Number - specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?min_length='
    url = path_url + format(len) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_max_length(len, page=1, pageSize=10):
    """
    This call returns list of structures which have length equal or smaller than len param.

    :param len: Number - specifies the maximum length
    :param page: Number -specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?max_length='
    url = path_url + format(len) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_min_max_length(min, max, page=1, pageSize=10):
    """
    This call returns list of structures which have length between min and max params.

    :param min: Number - specifies the minimum length
    :param max: Number - specifies the maximum length
    :param page: Number -specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?min_length=' + format(min) + '&max_length=' + format(
        max) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_by_database(database, page=1, pageSize=10):
    """
    This call returns list of structures which are in database param.

    :param database: String - Name of database
    :param page: Number - specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?database='
    url = path_url + format(database) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')


def filter_by_external_id(id):
    """
    This call provides details about structure from external_id.

    :param id: String - external id
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?external_id='
    url = path_url + format(id)
    try:
        request = urllib.request.Request(url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_database_min_length(database, min, page=1, pageSize=10):
    """
    This call returns list of structures which are in database param and have length bigger than min.

    :param database: String - Name of database
    :param min: Number - specifies the minimum length
    :param page: Number - specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?database=' + format(database) + '&min_length=' + format(
        min) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

def filter_database_max_length(database, max, page=1, pageSize=10):
    """
    This call returns list of structures which are in database param and have length smaller than max.

    :param database: String - Name of database
    :param max: Number - specifies the maximum length
    :param page: Number - specifies which page will be shown(1 is default)
    :param pageSize: Number - specifies how many scores will be shown in one page(10 is default, 100 is maximum)
    :return: count, publications, md5, rnacentral_id, length, xrefs, sequence, url, next, previous
    """
    path_url = 'http://rnacentral.org/api/v1/rna/?database=' + format(database) + '&max_length=' + format(
        max) + '&page=' + format(page) + '&page_size=' + format(pageSize)
    try:
        request = urllib.request.Request(path_url)
        temp = urllib.request.urlopen(request)
        result = temp.read()
        result = result.decode('unicode_escape')
        assert result
        result = json.loads(result)
        result = json.dumps(result, indent=4)
        '''root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close'''
        return result
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print('Not found')
        else:
            print('Invalid Input')

# This sequence has an RNAcentral id
# sequence = 'CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'
# md5 = calculate_md5(sequence)
# print(rnacentral_id(md5))
# print(information_RNACentral('URS0000000001'))
# print(publications_RNACentral('URS0000000001'))
# print(xrefs_RNACentral('URS0000000001'))
# print(filter_length(2014))
# print(filter_min_length(2014,3,5))
# print(filter_max_length(2014))
# print(filter_min_max_length(1000,2002))
# print(filter_by_database('srpdb'))
# print(filter_by_external_id('MIMAT0000091'))
# print(filter_database_min_length('srpdb',200))
# print(filter_database_max_length('srpdb', 200, 1, 5))
