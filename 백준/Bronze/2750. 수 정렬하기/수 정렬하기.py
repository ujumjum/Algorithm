def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 입력 처리
n = int(input())  # 숫자의 개수
arr = [int(input()) for _ in range(n)]

sorted_arr = bubble_sort(arr)

for num in sorted_arr:
    print(num)