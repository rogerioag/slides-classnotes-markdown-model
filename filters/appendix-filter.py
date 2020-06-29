# Converter tag [appendix] para \appendix do latex.
# [appendix]
####################
# pandoc native output: pandoc -s -t native appendix.txt
# [Para [Str "[appendix]"]]

import pandocfilters as pf
import re

tag_beamer = '\\appendix'

tag_latex = '\\appendix'

def latex(s):
    return pf.RawBlock('latex', s)

def mk_appendix(key, v, format, meta):
    import pdb
    #pdb.set_trace()
    if key == "Para":
        # v: [Str "[appendix]"]
        value = pf.stringify(v)
        # value tem [appendix]
        if value.startswith('[') and value.endswith(']'):
            matchObj = re.match(r'\[(.+?)\]', value, re.M|re.I)
            if matchObj:
                if matchObj.group(1) == "appendix":
                    if format == "beamer":
                        return latex(tag_beamer)
                    elif format == "latex":
                        return latex(tag_latex)

if __name__ == "__main__":
    pf.toJSONFilter(mk_appendix)
    