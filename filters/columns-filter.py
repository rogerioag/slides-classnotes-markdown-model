import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

def mk_columns(k, v, f, m):
    if k == "Para":
        value = pf.stringify(v)
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]
            if content == "columns":
                if f == "beamer":
                    return latex(r'\begin{columns}[T]')
                elif f == "latex":
                    return latex(r'\begin{multicols}{2}')
            elif content == "/columns":
                if f == "beamer":
                    return latex(r'\end{columns}')
                elif f == "latex":
                    return latex(r'\end{multicols}')
            elif content.startswith("column="):
                if f == "beamer":
                    return latex(r'\column{%s\textwidth}' % content[7:])
                elif f == "latex":
                    return latex(r'\columnbreak')

if __name__ == "__main__":

    pf.toJSONFilter(mk_columns)
    