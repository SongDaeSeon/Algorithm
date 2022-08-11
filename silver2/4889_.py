num = 0
while True:
    arr = input()
    num += 1
    count = 0 #여는 괄호 갯수
    answer = 0
    if arr[0] == '-':
        break
    else:
        for i in arr: #여는 괄호를 만났을 때
            if i == '{':
                count += 1
            else: #닫는 괄호를 만났을 때
                if count <= 0: #만약 이전에 여는 괄호가 없었다?
                    answer += 1
                    count += 1            
                else: #만약 이전에 여는 괄호가 있었다?
                    count -= 1
        answer += count//2
        print('{}. {}'.format(num, answer))