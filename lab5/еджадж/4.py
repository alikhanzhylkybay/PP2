import re
s=input()
x=re.findall(r"^[a-zA-Z].*\d$", s)
if x:
    print("Yes")
else:
    print("No")