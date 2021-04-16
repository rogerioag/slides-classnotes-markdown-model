import pandocfilters as pf
import re

# Converter tag background para um bloco latex.
# [background]{imagem.{png|pdf}}
# ## Frame normal
# [/background]
####################
# Latex que deve ser gerado:
#{
#	\usebackgroundtemplate{%
#		\tikz\node[opacity=0.20] {\vspace{-0.5cm}\hspace{-0.23cm};\includegraphics[height=\paperheight,width=\paperwidth]{figures/banner-cuda.pdf}};}
#	\begin{frame}
#    Content.
#   \end{frame}
#}

#[rag@chamonix tests]$ pandoc background.txt -s -t native
#Pandoc (Meta {unMeta = fromList []})
#[Para [Str "[background]{figures/banner-cuda.pdf}"]
#,Header 2 ("frame-t\237tulo",["fragile","allowframebreaks"],[]) [Str "Frame",Space,Str "T\237tulo"]
#,BulletList
# [[Plain [Str "Conte\250do."]]]
#,Para [Str "[/background]"]]
#[rag@chamonix tests]$ 

beamer_code = r'\{\usebackgroundtemplate\{%\n\tikz\node[opacity=0.2]\n\{\includegraphics[height=\paperheight,width=\paperwidth]\{filepath\}\};\}'
# begin_beamer = '{\n\usebackgroundtemplate{%\n\tikz\node[opacity=0.20] {\vspace{-0.5cm}\hspace{-0.23cm};\includegraphics[height=\paperheight,width=\paperwidth]{figures/banner-cuda.pdf}};}'
end_beamer = '}'

begin_latex = '\\vspace{-0.75cm}'

end_latex = ''

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
    