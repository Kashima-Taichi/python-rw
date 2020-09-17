# if not : 条件式の結果が真であれば偽、偽の場合は真
# 8-93

path = 'fileMnipulation/readfile/read.txt'

with open(path, 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        # 行数がなくなれば false となり while文は続行できなくなる
        if not line:
            break
