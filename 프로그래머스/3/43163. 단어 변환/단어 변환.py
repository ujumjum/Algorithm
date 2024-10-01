from collections import deque

def one_letter_diff(word1, word2):
    diff_cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            diff_cnt += 1
        if diff_cnt > 1:
            return False
        
    return diff_cnt == 1

def solution(begin, target, words):
    # target이 words에 없을 경우
    if target not in words:
        return 0
    
    # BFS
    queue = deque([(begin, 0)])     # 단어, 변환횟수 0
    
    visited = set()
    visited.add(begin)
    
    while queue:
        cur_word, steps = queue.popleft()
        
        if cur_word == target:
            return steps
        
        for word in words:
            if word not in visited and one_letter_diff(cur_word, word):
                visited.add(word)
                queue.append((word, steps+1))
                
    return 0