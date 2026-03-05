import re
s=input()
pattern=re.compile(r'\w+')
search=pattern.findall(s)
print(len(search))