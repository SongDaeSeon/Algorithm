num = int(input())

for i in range(num):
    a = list(input())
    count = 0

    for i in a:
        if i == '(':
            count +=1 # (가 나올때마다 1씩 더해줌)
        else:
            count -=1 #) 가 나올떄마다 1씩 뺴줌
            if count < 0: #)(가 나올경우 대비 ?)
                break
    if count == 0:
        print("YES") #()의 갯수가 맞는지 확인
    else:
        print("NO")