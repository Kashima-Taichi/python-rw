# withステートメントを使用すると、ファイルを閉じるコードが必要がないので、良いとされている
path = 'fileMnipulation/withStatement/with.txt'

with open('with.txt', 'w') as f:
    print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
