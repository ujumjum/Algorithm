n = int(input())  
m = int(input())  
s = input()  

count = 0  # IOI pattern count
result = 0 # pattern 몇개~?
i = 0

# 문자열 전체를 순회하면서 IOI 패턴 찾기
while i < m - 1:
    if s[i:i+3] == "IOI":
        count += 1  
        i += 2  # "IOI"에서 2칸 이동 (중복 패턴 확인 위해)
        if count == n:  # N번 반복된 패턴을 찾으면
            result += 1
            count -= 1  # 중복 패턴 처리를 위해 1 감소
    else:
        i += 1
        count = 0  # 패턴이 끊기면 초기화

print(result)