# n일 동안 사용할 금액, m 번만 빼서 사용
# k 최소 인출 금액 : 하루 필요 금액 감당
# - 최대 인출 금액 : 모든 날에 필요한 금액을 한 번에 인출(모든금액합)

# 하루 사용 금액이 limit을 넘지 않도록 m번 이하로 인출 가능한가?
def is_possible(limit, daily_money, n,m):
    cnt = 1         # 인출 횟수
    cur_sum = 0     # 현재 인출한 금액의 합

    # 하루치 금액을 하나씩 확인
    for money in daily_money:
        if cur_sum + money > limit:
            cnt+=1
            cur_sum = money     # 현재 인출 금액 초기화(해당 날의 금액만큼 인출)
        else:
            cur_sum += money    # 인출 가능하면 금액 ++++
    
    return cnt <= m

# 이진탐색
def min_withdraw(n, m, daily_money):
    left = max(daily_money)     # 최소 인출 금액
    right = sum(daily_money)    # 최대 인출 금액

    result = right

    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid, daily_money, n, m):
            result = mid
            right = mid-1
        else:
            left = mid + 1

    return result

n, m = map(int, input().split())
daily_money = [int(input()) for _ in range(n)]

answer = min_withdraw(n, m, daily_money)
print(answer)