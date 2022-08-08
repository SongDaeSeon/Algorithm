num = int(input())

for i in range(num):
    sen = input()
    left = [] 
    right = [] 
    for i in sen:
        if i == '<': #<가 들어오면 왼쪽 스택의 마지막 값을 오른쪽 스택에 붙임
            if len(left) > 0:
                right.append(left.pop())
        elif i == '>': #>가 들어오면 오른쪽 스택의 마지막 값을 왼쪽 스택에 붙임
            if len(right) > 0:
                left.append(right.pop())
        elif i == '-': #지움
            if len(left) > 0:
                left.pop()
        else: #문자저장
            left.append(i)

    left = ''.join(left) #리스트 방식을 해제
    right = ''.join(reversed(right))#reversed안해도 결과는맞는데 오류떠서 reversed하니 맞더라

    print(left + right)


