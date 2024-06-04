def solution(name):
    # 알파벳 리스트
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(name)
    min_move = n - 1  # 초기 커서 이동 횟수 (한쪽 방향으로 쭉 이동하는 경우)
    answer = 0
    
    for i in range(n):
        # 현재 문자가 'A'에서 몇 번째 떨어져 있는지 계산
        index = alphabet.index(name[i])
        # 위 또는 아래 방향으로 알파벳을 맞추는 최소 조작 횟수
        answer += min(index, 26 - index)
        
        # 다음 위치부터 연속된 A의 끝 위치 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 커서를 좌우로 이동하는 최소 이동 횟수 계산
        min_move = min(min_move, i + i + n - next_idx, 2 * (n - next_idx) + i)
    
    answer += min_move
    return answer