# -*- coding: utf-8 -*-

import re
from unicodedata import normalize
from django.utils.encoding import force_text



def normalize_text(text, delim='_'):
    """Generates an slightly worse ASCII-only."""
    normalized_text = force_text(
        normalize("NFKD", text).encode('ascii', 'ignore'))
    return re.sub(r'\s', '_', normalized_text)
