N = int(input())
sgCard = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

sgCard.sort()

# binary search
def binary_search(arr, target):
    start, end = 0, len(arr) -1
    
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid-1
    return 0

result = []
for num in card:
    result.append(binary_search(sgCard, num))

print(" ".join(map(str, result)))