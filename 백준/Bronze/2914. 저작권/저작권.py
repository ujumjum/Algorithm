songs, avg = map(int, input().split())

answer = songs * (avg - 1) + 1
print(answer)