import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

def mk_appendix(k, v, f, m):
    if k == "Para":
        value = pf.stringify(v)
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]
            if content == "appendix":
                if f == "beamer":
                    return latex(r'\appendix')
                elif f == "latex":
                    return latex(r'\vspace{-0.75cm}')

if __name__ == "__main__":

    pf.toJSONFilter(mk_appendix)
    