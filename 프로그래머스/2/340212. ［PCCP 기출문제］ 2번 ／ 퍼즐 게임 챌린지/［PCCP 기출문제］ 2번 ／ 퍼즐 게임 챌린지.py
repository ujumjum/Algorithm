def solution(diffs, times, limit):
    left = 1
    right = max(diffs)

    while left <= right:
        level = (left + right) // 2
        total = 0

        # 현재 level로 모든 퍼즐을 푸는 시간 계산
        for i in range(len(diffs)):
            if diffs[i] <= level:
                total += times[i]
            else:
                mistake = diffs[i] - level
                total += (times[i] + times[i - 1]) * mistake + times[i]

            # 이미 제한시간을 넘으면 더 계산할 필요 없음
            if total > limit:
                break

        # 제한시간 안에 가능하면 더 낮은 level 탐색
        if total <= limit:
            right = level - 1
        else:
            left = level + 1

    return left