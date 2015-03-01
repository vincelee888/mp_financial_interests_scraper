__author__ = 'Vince Lee'

import re
import collections

def parse(title):
    p = re.search('^([a-zA-Z -]*),\s([a-zA-Z .]*)\s\((.*)\)', title, re.UNICODE)
    ParsedTitle = collections.namedtuple('ParsedTitle', ['firstName', 'surname', 'constituency'])
    return ParsedTitle(p.group(2), p.group(1).title(), p.group(3))