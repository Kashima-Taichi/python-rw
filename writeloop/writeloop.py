path = 'fileMnipulation/writeloop/writeloop.txt'

f = open(path, 'w')

# ファイルの中身を削除する（ファイル自体は削除しない）
f.truncate(0)

for i in range(101):
    f.write(str(i) + '\n')

f.close()
