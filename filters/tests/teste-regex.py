#!/usr/bin/python

import csv, re
import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

# [Para [Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "Teste",SoftBreak,Str "Merda",SoftBreak,Str "[/terminal]"]]
# key: Para e value: [Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "Teste",SoftBreak,Str "Merda",SoftBreak,Str "[/terminal]"]
# Com o stringfy do value fica:
# [Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "Teste",SoftBreak,Str "Merda",SoftBreak,Str "[/terminal]"]

# value = '[Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "Teste",SoftBreak,Str "Merda",SoftBreak,Str "[/terminal]"]'

# value = '[Str "[terminal]",SoftBreak,Str "rogerio@chamonix:/for-directive$",Space,Str "./example-for-directive.exe",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "Before",Space,Str "parallel",Space,Str "region...",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "Working",Space,Str "in",Space,Str "0",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "Working",Space,Str "in",Space,Str "1",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "Working",Space,Str "in",Space,Str "2",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[3][1349605120]:",Space,Str "Working",Space,Str "in",Space,Str "12",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[3][1349605120]:",Space,Str "Working",Space,Str "in",Space,Str "13",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[3][1349605120]:",Space,Str "Working",Space,Str "in",Space,Str "14",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "Working",Space,Str "in",Space,Str "3",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[1][1366390528]:",Space,Str "Working",Space,Str "in",Space,Str "4",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[1][1366390528]:",Space,Str "Working",Space,Str "in",Space,Str "5",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[1][1366390528]:",Space,Str "Working",Space,Str "in",Space,Str "6",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[1][1366390528]:",Space,Str "Working",Space,Str "in",Space,Str "7",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[2][1357997824]:",Space,Str "Working",Space,Str "in",Space,Str "8",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[2][1357997824]:",Space,Str "Working",Space,Str "in",Space,Str "9",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[2][1357997824]:",Space,Str "Working",Space,Str "in",Space,Str "10",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[2][1357997824]:",Space,Str "Working",Space,Str "in",Space,Str "11",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[3][1349605120]:",Space,Str "Working",Space,Str "in",Space,Str "15",Space,Str "loop",Space,Str "iteration...",SoftBreak,Str "Thread[0][1378895744]:",Space,Str "After",Space,Str "parallel",Space,Str "region...",SoftBreak,Str "rogerio@chamonix:/for-directive$",SoftBreak,Str "[/terminal]"]'
value = '[Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "Teste",SoftBreak,Str "[/terminal]"]'

# result = re.findall('\[Str \"\[(.*?)\]\",(.*?),Str \"\[(.*?)\]\"\]', value, re.DOTALL)

# print(result)

# for x in result:
#	print x

# print("Teste:")
matchObj = re.match( r'\[Str \"\[(.*?)\]\",(.*?),Str \"\[(.*?)\]\"\].*', value, re.M|re.I)

if matchObj:
   # print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
   print "matchObj.group(3) : ", matchObj.group(3)

   code = matchObj.group(2).replace("Str", "").replace("SoftBreak", "\n").replace(",", "").replace("\"", "").replace("Space", " ")

   begin = matchObj.group(1).replace("terminal", "\\begin{terminal}")

   end = matchObj.group(3).replace("/terminal", "\end{terminal}")

   print(begin + code + end)
else:
   print "No match!!"





#str2 = str.replace("Str ", "").replace("Space", " ").split(",")

#for x in str2:
#	print x




