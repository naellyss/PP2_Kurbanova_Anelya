#task 1
import re

def match_pattern(text):
    pattern = r'^ab*$'
    return bool(re.match(pattern, text))

print(match_pattern("a"))
print(match_pattern("ab"))
print(match_pattern("abbb"))
print(match_pattern("ac"))

#task 2
import re

def match_pattern(text):
    pattern = r'^ab{2,3}$'
    return bool(re.match(pattern, text))

print(match_pattern("abb"))
print(match_pattern("abbb"))
print(match_pattern("ab"))
print(match_pattern("abbbb"))

#task 3
import re

def find_snake_case(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    return re.findall(pattern, text)

text = "hello_world test_var Normal_text abc_def_ghi"
print(find_snake_case(text))

#task 4
import re

def find_capitalized_words(text):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, text)

text = "Hello world Python RegEx TEST"
print(find_capitalized_words(text))

#task 5
import re

def match_pattern(text):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, text))

print(match_pattern("axxxb"))
print(match_pattern("ab"))
print(match_pattern("axc"))

#task 6
import re

def replace_delimiters(text):
    pattern = r'[ ,\.]'
    return re.sub(pattern, ':', text)

text = "Python, RegEx. Exercises test"
print(replace_delimiters(text))

#task 7
import re

def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

text = "hello_world_variable"
print(snake_to_camel(text))

#task 8
import re

def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'
    return [s for s in re.split(pattern, text) if s]

text = "SplitThisStringByUppercase"
print(split_at_uppercase(text))

#task 9
import re

def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', text)

text = "HelloWorldPythonRegEx"
print(insert_spaces(text))

#task 10
import re

def camel_to_snake(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', text).lower()

text = "camelCaseToSnakeCase"
print(camel_to_snake(text))


