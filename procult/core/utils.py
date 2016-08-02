# -*- coding: utf-8 -*-

import re
import os

from zipfile import ZipFile, ZIP_DEFLATED
from unicodedata import normalize
from uuid import UUID

from django.utils.encoding import force_text


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


def validate_uuid(uuid_string, version=4):
    try:
        value = UUID(uuid_string, version)
    except ValueError:
        return False
    return value.hex == uuid_string
