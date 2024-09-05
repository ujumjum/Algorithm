# 1~N 번, K 번째 사람 제거
# 1. 입력 
n, k = map(int, input().split())

# 2. K 번째 사람 제거 후 원만들어서 다시 k번째 사람 제거
def josephus(n,k):
    people = list(range(1, n+1))
    result = []
    out_index = 0

    while people:
        # 제거하고 원 만들기
        out_index = (out_index + k - 1) % len(people)
        result.append(people.pop(out_index))

    print("<"+ ", ".join(map(str, result)) + ">")

# 3. 출력 : 요세푸스 순열
josephus(n,k)