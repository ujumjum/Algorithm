# 배열 A -> 수열 P 적용한 결과 : 비내림차순(중복허용 오름차순)
n = int(input())
A = list(map(int, input().split()))

indexed_A = [(value, index) for index, value in enumerate(A)]

indexed_A.sort()

P = [0] * n

for sorted_index, (value, original_index) in enumerate(indexed_A):
    P[original_index] = sorted_index

print(' '.join(map(str, P)))