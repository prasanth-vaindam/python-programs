

path = "C:\\HemaSundar\\Day03\\extractWebsite.py"

last_slash = path.rfind('\\')

previous_slash =path.rfind("\\",0,last_slash)
print(path[previous_slash+1:last_slash])