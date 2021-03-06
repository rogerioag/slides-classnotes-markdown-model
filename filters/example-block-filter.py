# Converter tag terminal para um bloco. 
# [exampleblock]{Titulo}
# First line is the title.
# Others are the content of block.
# [/exempleblock]
####################
# Beamer que deve ser gerado:
# \begin{exampleblock}{First line is the title}
# Others are the content of block.
# \end{exampleblock}
# Latex que deve ser gerado:
# \begin{pabox}{First line is the title}
# Others are the content of block.
# \end{pabox}

import pandocfilters as pf
import csv, re

begin_beamer = '\begin{exampleblock}{Title}}'

end_beamer = '\end{exampleblock}'

begin_latex = '\\begin{pabox}{Title}'

end_latex = '\end{pabox}'

def mystringify(x):
    """Walks the tree x and returns concatenated string content with formatting.
    """
    result = []

    def go(key, val, format, meta):
        if key in ['Str', 'MetaString']:
            result.append(val)
        elif key == 'Code':
            result.append(val[1])
        elif key == 'Math':
            result.append(val[1])
        elif key == 'LineBreak':
            result.append("LineBreak")
        elif key == 'SoftBreak':
            result.append("SoftBreak")
        elif key == 'Space':
            result.append("Space")

    pf.walk(x, go, "", {})
    return ''.join(result)

# The pf.stringify() returns: "[terminal]  rogerio@chamonix:hello-world$  ./hello-world.exe  Hello  World!!!  Teste  [/terminal]"
# mystringify() returns: '"[terminal]SoftBreakrogerio@chamonix:hello-world$Space./hello-world.exeSoftBreakHelloSpaceWorld!!!SoftBreakTesteSoftBreak[/terminal]"

def latex(s):
    return pf.RawBlock('latex', s)

def mk_terminal(key, value, format, meta):
    # import pdb
    # pdb.set_trace()
    if key == "Para":
        val = mystringify(value).strip()
        if val.startswith('[') and val.endswith(']'):
            matchObj = re.match(r'\[(.*?)\]SoftBreak(.*?)SoftBreak\[(.*?)\].*', val, re.M|re.I)
            if matchObj:
                # print "matchObj.group() : ", matchObj.group()
                # print "matchObj.group(1) : ", matchObj.group(1)
                # print "matchObj.group(2) : ", matchObj.group(2)
                # print "matchObj.group(3) : ", matchObj.group(3)

                code = matchObj.group(2).replace("Str", "").replace("SoftBreak", "\n").replace(",", "").replace("\"", "").replace("Space", " ")

                if (format == "beamer"):
                    begin = matchObj.group(1).replace("exampleblock", begin_beamer) + '\n'
                    end = matchObj.group(3).replace("/exampleblock", end_beamer)
                elif (format == "latex"):
                    begin = matchObj.group(1).replace("exampleblock", begin_latex) + '\n'
                    end = matchObj.group(3).replace("/exampleblock", end_latex)   

                # return [latex(begin)] + [latex(code)] + [latex(end)]
                return [latex(begin + code + end)]


if __name__ == "__main__":
    pf.toJSONFilter(mk_terminal)
    