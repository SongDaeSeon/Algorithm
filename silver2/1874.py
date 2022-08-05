num = int(input())
first = [] #정수 저장하는 공간
last = [] #부호 저장하는 공간
count = 1 #1이 최솟값
result = True #이게 없으면 출력 오류가 뜬다ㅠㅠ 이건 구글링 쩔수

for i in range(num):
    a = int(input())
    while count <= a: #입력하는 수가 1보다 클동안
        first.append(count)
        count += 1
        last.append('+')

    if first[-1] == a: #top에 있는 숫자가 입력한 숫자랑 같으면?
        first.pop()
        last.append('-')
    else:
        result = False

if not result:
    print("NO")
else: 
    for i in last:
        print(i)



