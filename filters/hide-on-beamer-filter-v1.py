import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

def mk_hideonbeamer(k, v, f, m):
    if k == "Para":
        value = pf.stringify(v)
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]
            if content == "hideonbeamer":
                if f == "beamer":
                    return latex(r'\begin{comment}')
                elif f == "latex":
                    return latex(r'')
            elif content == "/hideonbeamer":
                if f == "beamer":
                    return latex(r'\end{comment}')
                elif f == "latex":
                    return latex(r'')

if __name__ == "__main__":

    pf.toJSONFilter(mk_hideonbeamer)
    