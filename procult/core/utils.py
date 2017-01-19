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

def compress_folder_files(dirname, zipname, zipfile):
    """Compress files in directory to zipped file"""
    
    files = [files for base, subdirs, files in os.walk(dirname)][0]

    # Change path to save zipped file in user folder
    os.chdir(dirname)

    for directory in os.walk(dirname):

        for filename in directory[2]:
            proposal_file = os.path.join(directory[0], filename)
            proposal_filepath = "/".join(dirname.split(os.sep)[-1:])
            proposal_filepath = "{directory}/{filename}".format(directory=proposal_filepath,
                                                               filename=proposal_file.split(os.sep)[-1])
            zipfile.write(proposal_file, proposal_filepath)

    return zipfile.filename

def _generate_proposalnumber():
    number = randint(1, 99999)
    Proposal = apps.get_model('core', 'Proposal')
    while len(Proposal.objects.filter(number=number)) != 0:
        number = randint(1, 99999)

    return number