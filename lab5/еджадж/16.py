import re
s=input()
match = re.search(r'Name: (.+), Age: (\d+)', s)
print(*match.groups())