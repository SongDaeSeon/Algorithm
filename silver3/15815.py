a = input()
arr = []

for i in a:
   if i in '+-*/':
        b = arr[-1]
        arr.pop()
        a = arr[-1]
        arr.pop()
        if i == '+':
            arr.append(a+b)
        if i == '-':
            arr.append(a-b)
        if i == '*':
            arr.append(a*b)
        if i == '/':
            arr.append(a//b)
   else:
        arr.append(int(i))
for i in arr:
    print(i)
