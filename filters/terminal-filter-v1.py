# Converter tag terminal para um bloco. 
# [terminal ]
# rogerio@chamonix:calculator-tutorial-2$ ./calculadora.exe 
# --(end of buffer or a NUL)
# 1+2
# --accepting rule at line 15 ("1")
# --accepting rule at line 20 ("+")
# --accepting rule at line 15 ("2")
# --accepting rule at line 20 ("")
# 3
# rogerio@chamonix:calculator-tutorial-2$
# [/terminal]
####################
# Latex que deve ser gerado:
# \setbeamercolor*{block title example}{fg=green!10,bg=gray!90}
# \setbeamercolor*{block body example}{fg=green, bg=black!80}
# \begin{exampleblock}{\centering {Terminal}}
#    \vspace{-0.3cm}
#    \begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]
# rogerio@chamonix:calculator-tutorial-2$ ./calculadora.exe 
# --(end of buffer or a NUL)
# 1+2
# --accepting rule at line 15 ("1")
# --accepting rule at line 20 ("+")
# --accepting rule at line 15 ("2")
# --accepting rule at line 20 ("")
# 3
# rogerio@chamonix:calculator-tutorial-2$
#   \end{lstlisting}
#   \vspace{-0.3cm}
# \end{exampleblock}

import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

def mk_terminal(key, value, format, meta):
    if key == "Para":
        val = pf.stringify(value)
        if val.startswith('[') and val.endswith(']'):
            content = val[1:-1]
            if content == "terminal":
                if (format == "beamer"):
                    return latex('\setbeamercolor*{block title example}{fg=darkgray!95!white,bg=darkgray!50!white}' + '\n' +
                                 '\setbeamercolor*{block body example}{fg=green!75!black,bg=black!80}' + '\n' + 
                                 '\\begin{exampleblock}{\centering {Terminal}}' + '\n' +
                                 '  \\vspace{-0.3cm}' + '\n' + 
                                 '  \\begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]'
                                 )
                elif (format == "latex"):
                    return latex('\\begin{terminalbox}{}{' + '\n' +
                                 '  \\begin{lstlisting}[style=bash, frame=none, numbers=none, xleftmargin=0pt, framexleftmargin=0pt]' 
                                )
            elif content == "/terminal":
                if (format == "beamer"):
                    return latex('  \end{lstlisting}' + '\n' + '  \\vspace{-0.3cm}' + '\n' + '\end{exampleblock}')
                elif (format == "latex"):
                    return latex('  \end{lstlisting}' + '\n' + '}\end{terminalbox}')

if __name__ == "__main__":
    pf.toJSONFilter(mk_terminal)
    