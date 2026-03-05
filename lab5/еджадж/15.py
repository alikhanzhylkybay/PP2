import re
s=input()
def double_digits(match):
    digit = match.group(0)
    return digit * 2

result = re.sub(r'\d', double_digits, s)
print(result)
