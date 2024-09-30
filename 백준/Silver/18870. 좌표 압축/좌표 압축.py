n = int(input())
coords = list(map(int, input().split()))

sorted_coords = sorted(set(coords))
# quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     mid = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + mid + quick_sort(right)

# sorted_coords = quick_sort(list(set(coords)))

compress_map = {coord: idx for idx, coord in enumerate(sorted_coords)}

compressed_coords = [compress_map[coord] for coord in coords]
print(' '.join(map(str, compressed_coords)))