
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeInString = 'import os\nos.system("ls")'
codeObject = compile(codeInString, 'sumstring', 'exec')
print(codeObject)
exec(codeObject)
