import re
s=input()
pattern=re.compile(r'(\d{2})(/)(\d{2})(/)(\d{4})')
search=pattern.findall(s)
print(len(search))