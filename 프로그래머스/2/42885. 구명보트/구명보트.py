def solution(people, limit):
    # 사람들의 몸무게를 오름차순으로 정렬합니다.
    people.sort()
    light = 0
    heavy = len(people) - 1
    boats = 0
    
    # 양 끝에서 시작하여 가장 가벼운 사람과 가장 무거운 사람을 짝지어봅니다.
    while light <= heavy:
        # 가장 무거운 사람과 가장 가벼운 사람을 함께 태울 수 있는 경우
        if people[light] + people[heavy] <= limit:
            light += 1
        # 가장 무거운 사람을 태우는 경우
        heavy -= 1
        # 보트 하나 사용
        boats += 1
    
    return boats