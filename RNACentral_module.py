import hashlib
import requests
import urllib.request
import json
import tkinter as tk
from tkinter import filedialog


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
    except:
        print('Invalid Input')


def publications_RNACentral(id):
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
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except:
        print('Invalid Input')


def xrefs_RNACentral(id):
    path_url = 'http://rnacentral.org/api/v1/rna/' + format(id) + '/xrefs'
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
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        if file_path:
            file = open(file_path + '.txt', 'w')
            file.write(result)
            file.close
        return result
    except:
        print('Invalid Input')


def filter_length(len):
    path_url = 'http://rnacentral.org/api/v1/rna/?length='
    url = path_url + format(len)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_min_length(len):
    path_url = 'http://rnacentral.org/api/v1/rna/?min_length='
    url = path_url + format(len)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_max_length(len):
    path_url = 'http://rnacentral.org/api/v1/rna/?max_length='
    url = path_url + format(len)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_min_max_length(min, max):
    path_url = 'http://rnacentral.org/api/v1/rna/?min_length=' + format(min) + '&max_length=' + format(max)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_by_database(database):
    path_url = 'http://rnacentral.org/api/v1/rna/?database='
    url = path_url + format(database)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_by_external_id(id):
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_database_min_length(database, min):
    path_url = 'http://rnacentral.org/api/v1/rna/?database=' + format(database) + '&min_length=' + format(min)
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
            print('Not found')
        else:
            print('Invalid Input')


def filter_database_max_length(database, max):
    path_url = 'http://rnacentral.org/api/v1/rna/?database=' + format(database) + '&max_length=' + format(max)
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
            print('Not found')
        else:
            print('Invalid Input')


sequence = 'CUGAAUAAAUAAGGUAUCUUAUAUCUUUUAAUUAACAGUUAAACGCUUCCAUAAAGCUUUUAUCCA'
md5 = calculate_md5(sequence)
# print(rnacentral_id(md5))
# print(information_RNACentral('1cbs'))
# print(publications_RNACentral('URS0000000001'))
# print(xrefs_RNACentral('URS0000000001'))
# print(filter_length(2014))
# print(filter_min_length(2014))
# print(filter_max_length(2014))
# print(filter_min_max_length(100,200))
# print(filter_by_database('srpdb'))
# print(filter_by_external_id('MIMAT0000091'))
# print(filter_database_min_length('srpdb',200))
# print(filter_database_max_length('srpdb',200))
