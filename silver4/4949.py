while True:
    sen = input()
    arr = [] 
    count = 0 #짝이 안맞으면 더해주는거
    if sen == '.': #.치면 종료
        break
    for i in sen:
        if i == '(': #(있으면 스택에 붙여줌
            arr.append(i)
        elif i == ')': 
            if arr and arr[-1] == '(': #스택에 (가 있으면 pop
                arr.pop()
            else:
                count += 1 #없으면 +1
                break
        if i == '[':
            arr.append(i)
        elif i == ']':
            if arr and (arr[-1] == '['):
                arr.pop()
            else:
                count += 1
                break
    if not arr and count == 0: 
        print("yes")
    else:
        print("no")







