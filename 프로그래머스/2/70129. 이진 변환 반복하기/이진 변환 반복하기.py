def solution(s):
    answer = [0, 0]  # [이진 변환 횟수, 0 제거 횟수]
    
    while s != "1":
        answer[1] += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:] # 2진수
        answer[0] += 1  # 변환횟수 증가
    
    return answer
