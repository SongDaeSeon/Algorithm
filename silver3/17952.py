import sys
input = sys.stdin.readline
num = int(input())

score, time, stack = [], [], []

for i in range(num):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        score.append(arr[1])
        time.append(arr[2])

    if time: 
        time[-1] -= 1 #시간이 있다면 -1
        if time[-1] == 0:
            stack.append(score.pop())
            time.pop()
print(sum(stack))
        


