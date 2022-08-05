import sys
num = int(input())
arr = []

for i in range(num):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        arr.append(word[1])   
    elif word[0] == 'pop':
        if len(arr) > 0:
            print(arr[-1])
            arr.pop(-1)
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(arr))
    elif word[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
        