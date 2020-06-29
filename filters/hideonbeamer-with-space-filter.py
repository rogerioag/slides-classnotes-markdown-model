# Converter tag hideonbeamer para um comentario no beamer. 
# ## Aparece somente nas notas de aula
#
# [hideonbeamer]
# * Item
#    + Item 2
#        - Item 3
# [/hideonbeamer]
####################
# pandoc native output: pandoc -s -t native hideonbeamer.txt

# [Header 2 ("aparece-somente-nas-notas-de-aula",[],[]) [Str "Aparece",Space,Str "somente",Space,Str "nas",Space,Str "notas",Space,Str "de",Space,Str "aula"]
# ,Para [Str "[hideonbeamer]",SoftBreak,Str "*",Space,Str "Item",SoftBreak,Str "+",Space,Str "Item",Space,Str "2",SoftBreak,Str "-",Space,Str "Item",Space,Str "3",SoftBreak,Str "[/hideonbeamer]"]]

####################
# No beamer que deve ser gerado:
# \begin{comment}
# \begin{itemize}
#    \item Item 
#    \begin{itemize}
#       \item Item 2
#       \begin{itemize}
#          \item Item 3
#       \end{itemize}
#    \end{itemize}
# \end{itemize}
# \end{comment}
####################
# No latex que deve ser gerado:
# \begin{itemize}
#    \item Item 
#    \begin{itemize}
#       \item Item 2
#       \begin{itemize}
#          \item Item 3
#       \end{itemize}
#    \end{itemize}
# \end{itemize}
# Pandoc (Meta {unMeta = fromList []})

# hideonbeamer.txt:
# [hideonbeamer]
# Teste de nota oculta
# [/hideonbeamer]
#
# hideonbeamer_spaced.txt
# [hideonbeamer]
#
# Teste de nota oculta
#
# [/hideonbeamer]

# Saida do haskell:
# rag@chamonix:/dados/aulas-aoc/aulas/md/filters$ pandoc -s -t native hideonbeamer.txt
# [Pandoc (Meta {unMeta = fromList []})
# [Para [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]]
#
# rag@chamonix:/dados/aulas-aoc/aulas/md/filters$ pandoc -s -t native hideonbeamer_spaced.txt
# Pandoc (Meta {unMeta = fromList []})
#[Para [Str "[hideonbeamer]"]
#,Para [Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta"]
#,Para [Str "[/hideonbeamer]"]]

import pandocfilters as pf
import re

begin_beamer = '\\vspace{-0.3cm}\n\\begin{comment}'

end_beamer = '\end{comment}'

begin_latex = '\\vspace{-0.8cm}'

end_latex = '\\vspace{-0.2cm}'

# The pf.stringify() returns: "[terminal]  rogerio@chamonix:hello-world$  ./hello-world.exe  Hello  World!!!  Teste  [/terminal]"
# mystringify() returns: '"[terminal]SoftBreakrogerio@chamonix:hello-world$Space./hello-world.exeSoftBreakHelloSpaceWorld!!!SoftBreakTesteSoftBreak[/terminal]"

# Saida do haskell:
# rag@chamonix:/dados/aulas-aoc/aulas/md/filters$ pandoc -s -t native hideonbeamer.txt
# [Pandoc (Meta {unMeta = fromList []})
# [Para [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]]

# The pf.stringify() returns: "[hideonbeamer]  Teste  de  nota  oculta  [/hideonbeamer]"
# mystringify() returns: 


def latex(s):
    return pf.RawBlock('latex', s)

#
# rag@chamonix:/dados/aulas-aoc/aulas/md/filters$ pandoc -s -t native hideonbeamer_spaced.txt
# Pandoc (Meta {unMeta = fromList []})
#[Para [Str "[hideonbeamer]"]
#,Para [Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta"]
#,Para [Str "[/hideonbeamer]"]]

def mk_hideonbeamer_spaced(key, v, format, meta):
    import pdb
    #pdb.set_trace()
    # val = mystringify('[Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]')
    # print (val)
    # [Para [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]]
    # key: Para, value: [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]

    if key == "Para":
        # v: [Str "[hideonbeamer]"]
        value = pf.stringify(v)
        # value tem [hideonbeamer]
        if value.startswith('[') and value.endswith(']'):
            matchObj = re.match(r'\[(.+?)\]', value, re.M|re.I)
            if matchObj:
                if matchObj.group(1) == "hideonbeamer":
                    if format == "beamer":
                        return latex(begin_beamer)
                    elif format == "latex":
                        return latex(begin_latex)
                elif matchObj.group(1) == "/hideonbeamer":
                    if format == "beamer":
                        return latex(end_beamer)
                    elif format == "latex":
                        return latex(end_latex)

if __name__ == "__main__":
    pf.toJSONFilter(mk_hideonbeamer_spaced)
    