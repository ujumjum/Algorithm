from itertools import combinations

while True:
    # 입력 받아 리스트로 변환
    case = list(map(int, input().split()))

    if case[0] == 0:
        break

    k = case[0]
    S = case[1:]

    result = combinations(S, 6)

    for comb in result:
        print(" ".join(map(str,comb)))

    # 빈줄
    print()