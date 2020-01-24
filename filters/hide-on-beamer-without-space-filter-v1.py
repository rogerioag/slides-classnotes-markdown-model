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
import csv, re

begin_beamer = '\\begin{comment}'

end_beamer = '\end{comment}'

begin_latex = ''

end_latex = ''

def mystringify(x):
    """Walks the tree x and returns concatenated string content with formatting.
    """
    result = []

    # Input: [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]
    # Output: [hideonbeamer]SoftBreakTesteSpacedeSpacenotaSpaceocultaSoftBreak[/hideonbeamer]

    def go(key, val, format, meta):
        if key in ['Str', 'MetaString']:
            result.append(val)
            # "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"
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

# Saida do haskell:
# rag@chamonix:/dados/aulas-aoc/aulas/md/filters$ pandoc -s -t native hideonbeamer.txt
# [Pandoc (Meta {unMeta = fromList []})
# [Para [Str "[hideonbeamer]",SoftBreak,Str "Teste",Space,Str "de",Space,Str "nota",Space,Str "oculta",SoftBreak,Str "[/hideonbeamer]"]]

# The pf.stringify() returns: "[hideonbeamer]  Teste  de  nota  oculta  [/hideonbeamer]"
# mystringify() returns: 


def latex(s):
    return pf.RawBlock('latex', s)


incomment = False

def mk_hideonbeamer_without_space(key, value, format, meta):
    
  

    #if key == "Para":
        # val = mystringify(value).strip()
    #    return(latex('\\textbf{'+ mystringify(value[0]) +'}'))

    
        #if val.startswith('[') and val.endswith(']'):
        #    # return(latex(val) + latex('\\begin{comment}'))
        #    # matchObj = re.match(r'\[(.*?)\]\n(.*?)\n\[(.*?)\].*', val, re.M|re.I)
        #    matchObj = re.match(r'\[(.*?)\].*', val, re.M|re.I)

        ##matchObj = re.match(r'\[(.*?)\]SoftBreak(.*?)SoftBreak\[(.*?)\].*', val, re.M|re.I)
        ##matchObj = re.match(r'\[(.*?)\](.*?)\[(.*?)\].*', val, re.M|re.I)
        
        #    return [latex(matchObj.group(1))]

        #    if matchObj:
                #print "[debug][hideonbeamer]: matchObj.group() : ", matchObj.group()
                #print "matchObj.group(1) : ", matchObj.group(1)
                #print "matchObj.group(2) : ", matchObj.group(2)
                #print "matchObj.group(3) : ", matchObj.group(3)
                # pdb.set_trace()
        #        code = matchObj.group(2).replace("Str", "").replace("SoftBreak", "\n").replace(",", "").replace("\"", "").replace("Space", " ")


        #        if (format == "beamer"):
        #            begin = matchObj.group(1).replace("hideonbeamer", begin_beamer) + '\n'
        #            end = matchObj.group(3).replace("/hideonbeamer", end_beamer)
        #        elif (format == "latex"):
        #            begin = matchObj.group(1).replace("hideonbeamer", begin_latex) + '\n'
        #            end = matchObj.group(3).replace("/hideonbeamer", end_latex)   

        #        return [latex(begin + code + end)]


if __name__ == "__main__":
    pf.toJSONFilter(mk_hideonbeamer_without_space)
    