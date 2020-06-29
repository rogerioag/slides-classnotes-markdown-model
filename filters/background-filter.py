import pandocfilters as pf
import re

# {
# \usebackgroundtemplate{%
#		\tikz\node[opacity=0.2] {\includegraphics[height=\paperheight,width=\paperwidth]{figuras/tux-search.png}};}
#\begin{frame}{Perguntas?}
#\protect\hypertarget{perguntas}{}
#\Large
#\centering

#\textbf{Prof.~Rogério Aparecido Gonçalves}

#\url{rogerioag@utfpr.edu.br}
#\end{frame}
#}

beamer_code = r'\{\usebackgroundtemplate\{%\n\tikz\node[opacity=0.2]\n\{\includegraphics[height=\paperheight,width=\paperwidth]\{filepath\}\};\}'

latex_code = '\\vspace{-0.75cm}'

def latex(s):
    return pf.RawBlock('latex', s)

def mk_background(k, v, f, m):
    # [Para [Str "[background]{figuras/tux-search.png}"]]
    if k == "Para":
        # v: [Str "[background]{figuras/tux-search.png}"]
        value = pf.stringify(v)
        # value tem "[background]{figuras/tux-search.png}"
        # m = re.match(r'.*\[(.+?)\](\{(.+?)\})?.*', value)
        result = ''
        if value.startswith('[') and (value.endswith(']') or value.endswith('}')):
            matchObj = re.match(r'\[(.+?)\](\{(.+?)\})?', value, re.M|re.I)
            if matchObj:
                if matchObj.group(1) in {"background"}:
                    if f == "beamer":
                        result = beamer_code.replace("filepath", matchObj.group(2))
                    elif f == "latex":
                        result = latex_code
                
                return latex(result)

if __name__ == "__main__":
    pf.toJSONFilter(mk_background)
    