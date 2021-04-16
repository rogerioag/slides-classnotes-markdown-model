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

import pandocfilters as pf
import csv, re

begin_beamer = r'\{\usebackgroundtemplate\{%\n\tikz\node[opacity=0.2]\n\{\includegraphics[height=\paperheight,width=\paperwidth]\{filepath\}\};\}'

end_beamer = '}'

begin_latex = ''

end_latex = ''

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
    return pf.Raw
    lock('latex', s)

def mk_background(key, value, format, meta):
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
                    begin = matchObj.group(1).replace("background", begin_beamer) + '\n'
                    end = matchObj.group(3).replace("/background", end_beamer)
                elif (format == "latex"):
                    begin = matchObj.group(1).replace("background", begin_latex) + '\n'
                    end = matchObj.group(3).replace("/background", end_latex)   

                # return [latex(begin)] + [latex(code)] + [latex(end)]
                return [latex(begin + code + end)]


if __name__ == "__main__":
    pf.toJSONFilter(mk_background)
    