# 수빈 n(걷기 +-1, 순간이동 2*x), 동생 k
def seek_time(n, k):
    max_limit = 100001
    times = [-1]*max_limit
    times[n] = 0

    queue = [n]
    
    # BFS
    while queue:
        cur = queue.pop(0)

        if cur == k:
            return times[cur]
        
        for next_pos in (cur-1, cur+1, 2*cur):
            if 0 <= next_pos < max_limit and times[next_pos] == -1:
                times[next_pos] = times[cur] + 1
                queue.append(next_pos)

n, k = map(int, input().split())
answer = seek_time(n, k)

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
print(answer)