#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def match_a_followed_by_b(text):
    return bool(re.fullmatch(r'ab*', text))
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
def match_a_followed_by_2_3_b(text):
    return bool(re.fullmatch(r'ab{2,3}', text))
#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def find_lowercase_underscore(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)
#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
def find_upper_followed_by_lower(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def match_a_anything_b(text):
    return bool(re.fullmatch(r'a.*b', text))
# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def task6():
    text = "Hello, world. How are you?"
    print(re.sub(r'[ ,.]', ':', text))

# 7. Write a python program to convert snake case string to camel case string.

def task7():
    text = "hello_world_python"
    result = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)
    print(result)

# 8. Write a Python program to split a string at uppercase letters.

def task8():
    text = "HelloWorldPython"
    print(re.split(r'(?=[A-Z])', text))

# 9. Write a Python program to insert spaces between words starting with capital letters.

def task9():
    text = "HelloWorldPython"
    print(re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text))

# 10. Write a Python program to convert a given camel case string to snake case.

def task10():
    text = "helloWorldPython"
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    print(result)

