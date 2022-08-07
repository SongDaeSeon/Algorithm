num = int(input())
count = 0
for i in range(num):
    word = input()
    arr = []
    for i in range(len(word)):
        if arr:     
            if arr[-1] == word[i]: #arr top이랑 들어온거랑 확인 일치하면
                arr.pop()
            else:
                arr.append(word[i]) #일치하지 않으면
        else:
                arr.append(word[i]) #arr에 아무것도 없으면 append
    if not arr: #arr가 비었으면
        count += 1  
print(count)