import pandocfilters as pf
import re

begin_beamer = '\\begin{type}{title}'

end_beamer = '\end{type}'

begin_latex = '\\begin{type}{title}'

end_latex = '\end{type}\n\\vspace{0.3cm}'

def latex(s):
    return pf.RawBlock('latex', s)

def mk_exampleblock(k, v, f, m):
    # [Para [Str "[exampleblock]{T\x9ftulo}"]] -> [k,v]
    # [Para [Str "[exampleblock][T\237tulo]"]]
    if k == "Para":
        # v: [Str "[exampleblock][T\x9ftulo]"]
        value = pf.stringify(v)
        # value tem "[exampleblock]{T\x9ftulo}"
        # m = re.match(r'.*\[(.+?)\](\{(.+?)\})?.*', value)
        result = ''
        if value.startswith('[') and (value.endswith(']') or value.endswith('}')):
            matchObj = re.match(r'\[(.+?)\](\{(.+?)\})?', value, re.M|re.I)
            if matchObj:
                if matchObj.group(1) in {"block", "exampleblock", "alertblock"}:
                    if f == "beamer":
                        reptype = begin_beamer.replace("type", matchObj.group(1))
                        result = reptype.replace("title", matchObj.group(3))
                    elif f == "latex":
                        # result = begin_latex.replace("title", matchObj.group(3))
                        reptype = begin_latex.replace("type", matchObj.group(1) + 'box')
                        result = reptype.replace("title", matchObj.group(3))
                elif matchObj.group(1) in {"/block", "/exampleblock", "/alertblock"}:
                    if f == "beamer":
                        result = end_beamer.replace("type", matchObj.group(1).partition("/")[2])
                    elif f == "latex":
                        result = end_latex.replace("type", matchObj.group(1).partition("/")[2] + 'box')
                
                return latex(result)

if __name__ == "__main__":
    pf.toJSONFilter(mk_exampleblock)
    