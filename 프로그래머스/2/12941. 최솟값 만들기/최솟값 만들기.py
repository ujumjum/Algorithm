def solution(A,B):
    answer = 0
    # sum(A 원소 * B 원소) 최소값 찾기
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer