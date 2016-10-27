# -*- coding: utf-8 -*-

import re
import os
from zipfile import ZipFile, ZIP_DEFLATED
from random import randint
from unicodedata import normalize
from django.utils.encoding import force_text
from django.apps import apps

def normalize_text(text, delim='_'):
    """Generates an slightly worse ASCII-only."""
    normalized_text = force_text(
        normalize("NFKD", text).encode('ascii', 'ignore'))
    return re.sub(r'\s', '_', normalized_text)


def compress_files(dirname, zipname):
    """Compress files in directory to zipped file"""
    name = "{zipname}.zip".format(zipname=zipname)
    files = [files for base, subdirs, files in os.walk(dirname)][0]

    # Change path to save zipped file in user folder
    os.chdir(dirname)
    os.chdir('..')
    zip_path = os.getcwd()

    zipfile = ZipFile(os.path.join(zip_path, name), mode='w',
                      compression=ZIP_DEFLATED)
    pathlen = len(dirname) + 1
    print(files)
    for filename in files:
        proposal_file = os.path.join(dirname, filename)
        zipfile.write(proposal_file, proposal_file[pathlen:])
    zipfile.close()
    return zipfile.filename

def compress_all_files(dirname, zipname):
    """Compress files in directory to zipped file"""
    name = "{zipname}.zip".format(zipname=zipname)
    files = [files for base, subdirs, files in os.walk(dirname)][0]

    # Change path to save zipped file in user folder
    os.chdir(dirname)
    os.chdir('..')
    zip_path = os.getcwd()

    zipfile = ZipFile(os.path.join(zip_path, name), mode='w',
                      compression=ZIP_DEFLATED)
    pathlen = len(dirname) + 1
    isFirst = True
    for directory in os.walk(dirname):
        # Skip files in root directory, as another .zip files generated will be there
        if isFirst:
            isFirst = False
            continue

        for filename in directory[2]:
            print(directory[0])
            proposal_file = os.path.join(directory[0], filename)
            zipfile.write(proposal_file, proposal_file[pathlen:])

    zipfile.close()
    return zipfile.filename

def _generate_proposalnumber():
    number = randint(1, 99999)
    Proposal = apps.get_model('core', 'Proposal')
    while len(Proposal.objects.filter(number=number)) != 0:
        number = randint(1, 99999)

    return number