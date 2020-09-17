import string

with open('material/material.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(lang='python')
print(contents)
