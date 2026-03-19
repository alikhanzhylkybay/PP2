s = input()
vowels='aeiouAEIOU'
def any(s):
    for i in s:
        if i in vowels:
            return True
    return False
if any(s):
    print("Yes")
else:
    print("No")