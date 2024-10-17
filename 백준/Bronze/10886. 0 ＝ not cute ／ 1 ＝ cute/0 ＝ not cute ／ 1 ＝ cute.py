n = int(input())
cute_cnt = 0

for _ in range(n):
    is_cute = int(input())
    if is_cute == 1:
        cute_cnt +=1

print("Junhee is cute!" if cute_cnt > n // 2 else "Junhee is not cute!")