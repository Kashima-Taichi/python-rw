path = 'fileMnipulation/seek/seek.txt'

with open(path, 'r') as f:
    print(f.tell())
    print(f.read(1))
    print('#####')
    f.seek(5)
    print(f.tell())
    print(f.read(1))
    print('#####')
    f.seek(14)
    print(f.tell())
    print(f.read(1))
