num = int(input())
arr = []

for i in range(num):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))