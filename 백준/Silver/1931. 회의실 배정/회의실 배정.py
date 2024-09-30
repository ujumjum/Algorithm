# 각 회의가 겹치기 않게 회의실을 사용할 수 있는 회의의 최대 개수
n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int,input().split())
    meetings.append((start, end))   # 튜플로 추가

# 종료 시간 기준으로 정렬
meetings.sort(key=lambda x : (x[1], x[0]))

# sorted vs. sort
# sorted : 원본 유지하면서 정렬된 새로운 리스트 반환
# sort : 리스트 자체를 변경

# greedy
last_end_time = 0   # 마지막으로 선택된 회의의 종료 시간   
cnt = 0             # 회의 개수

for start, end in meetings:
    if start >= last_end_time :     # 현재 회의 시작 시간이 이전 회의 종료 시간 이후일 때
        cnt += 1                    # 회의 가능~
        last_end_time = end         # 현재 회의 종료시간 update

# 최대 사용할 수 있는 회의의 최대 개수
print(cnt)