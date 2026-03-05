import re
s=input()
x=re.findall(r'\d',s)
if x:
    print(*x, sep=" ")
else:
    print("")