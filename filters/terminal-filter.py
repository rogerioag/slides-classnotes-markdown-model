# Converter tag terminal para um bloco. 
# [terminal]
# rogerio@chamonix:$ ./hello.exe 
# Hello World!
# rogerio@chamonix:$
# [/terminal]
####################
# Latex que deve ser gerado:
# \setbeamercolor*{block title example}{fg=green!10,bg=gray!90}
# \setbeamercolor*{block body example}{fg=green, bg=black!80}
# \begin{exampleblock}{\centering {Terminal}}
# \vspace{-0.3cm}
# \begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]
# rogerio@chamonix:$ ./hello.exe 
# Hello World!
# rogerio@chamonix:$
# \end{lstlisting}
# \vspace{-0.3cm}
# \end{exampleblock}

import pandocfilters as pf
import csv, re

begin_beamer = '\setbeamertemplate{blocks}[rounded][shadow=false]\n\setbeamercolor*{block title example}{fg=darkgray!95!white,bg=darkgray!50!white}\n\setbeamercolor*{block body example}{fg=green!75!black,bg=black!80} \\begin{exampleblock}{\centering {Terminal}}\n\\vspace{-0.4cm}\n\\begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]'

end_beamer = '\end{lstlisting}\n\\vspace{-0.3cm}\n\end{exampleblock}'

begin_latex = '\\begin{terminalbox}{}{\n\\vspace{-0.3cm}\n\\begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]'

end_latex = '\end{lstlisting}}\n\\vspace{-0.3cm}\n\end{terminalbox}\n\\vspace{0.3cm}'

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
                    begin = matchObj.group(1).replace("terminal", begin_beamer) + '\n'
                    end = matchObj.group(3).replace("/terminal", end_beamer)
                elif (format == "latex"):
                    begin = matchObj.group(1).replace("terminal", begin_latex) + '\n'
                    end = matchObj.group(3).replace("/terminal", end_latex)   

                # return [latex(begin)] + [latex(code)] + [latex(end)]
                return [latex(begin + code + end)]


if __name__ == "__main__":
    pf.toJSONFilter(mk_terminal)
    