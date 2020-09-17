s = """\
AAA
BBB
CCC
DDD
"""

# 実行の位置によってファイルの位置を変える必要がある path = 'fileMnipulation/rw/rw.txt'
path = 'rw.txt'

# w+ で書き込みができる
with open(path, 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())
