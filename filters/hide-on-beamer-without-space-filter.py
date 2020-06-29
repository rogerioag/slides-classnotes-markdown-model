#!/usr/bin/env python

"""
Pandoc filter to comment text on beamer.
"""

import pandocfilters as pf
import re

begin_beamer = '\\begin{comment}'

end_beamer = '\end{comment}'

begin_latex = ''

end_latex = ''


def caps(key, value, format, meta):
    if key == 'Str':
        val = pf.Str(value)
        matchObj = re.match(r'(.*?)hideonbeamer(.*?)/hideonbeamer(.*?)\].*', val, re.M|re.I)
        return [latex(matchObj.group(1))]

if __name__ == "__main__":
    pf.toJSONFilter(caps)