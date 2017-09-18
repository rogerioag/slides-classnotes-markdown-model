# [Str "[terminal]",SoftBreak,Str "rogerio@chamonix:hello-world$",Space,Str "./hello-world.exe",SoftBreak,Str "Hello",Space,Str "World!!!",SoftBreak,Str "[/terminal]"]]


str = "[Str '[terminal]',SoftBreak,Str 'rogerio@chamonix:hello-world$',Space,Str './hello-world.exe',SoftBreak,Str 'Hello',Space,Str 'World!!!',SoftBreak,Str '[/terminal]']"

str2 = str.replace("Str ", "").replace("Space", " ").split(",")

for x in str2:
	print x
