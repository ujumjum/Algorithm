# n명 이름 / 국,영,수 조건따라 성적 정렬
def sorted_info(info):
    # 1. 국어 점수 감소하는 순서
    # 2. 국어 점수가 같다면, 영어 점수가 증가하는 순서
    # 3. 국어, 영어 같다면, 수학 점수가 감소하는 순서
    # 4. 모든 점수 같다면, 이름이 사전 순으로 증가하는 순서(대문자가 앞)
    return sorted(info, key=lambda x : (-x[1], x[2], -x[3], x[0]))

# merge sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) //2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)

# def merge(left, right):
    # result = []
    # i = j= 0

    # while i < len(left) and j < len(right):
    #     # 국어 내림차순
    #     if left[i][1] > right[j][1]:
    #         result.append(left[i])
    #         i += 1
    #     elif left[i][1] < right[j][1]:
    #         result.append(right[j])
    #         j += 1
    #     else:
    #         # 영어 오름차순
    #         if left[i][2] < right[j][2]:
    #             result.append(left[i])
    #             i += 1
    #         elif left[i][2] > right[j][2]:
    #             result.append(right[j])
    #             j += 1
    #         else:
    #             # 국어와 영어 점수가 같을 때 수학 점수를 비교 (내림차순)
    #             if left[i][3] > right[j][3]:
    #                 result.append(left[i])
    #                 i += 1
    #             elif left[i][3] < right[j][3]:
    #                 result.append(right[j])
    #                 j += 1
    #             else:
    #                 # 모든 점수가 같을 때 이름을 사전순으로 비교 (오름차순)
    #                 if left[i][0] < right[j][0]:
    #                     result.append(left[i])
    #                     i += 1
    #                 else:
    #                     result.append(right[j])
    #                     j += 1
    
    # result.extend(left[i:])
    # result.extend(right[j:])
    # return result


n = int(input())
info = []
for _ in range(n):
    name, ko, en, math = input().split()
    info.append((name, int(ko), int(en), int(math)))

sorted_info_list = sorted_info(info)

for student in sorted_info_list:
    print(student[0])