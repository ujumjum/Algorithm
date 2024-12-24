def solution(n, words):
    used_words = set()  # 이미 사용한 단어를 기록하는 집합
    last_word = words[0][0]  # 첫 번째 단어의 첫 글자
    for i in range(len(words)):
        word = words[i]
        
        # 1. 이전 단어의 마지막 글자와 현재 단어의 첫 글자가 맞지 않으면
        if word[0] != last_word:
            return [(i % n) + 1, (i // n) + 1]
        
        # 2. 이미 사용된 단어인 경우
        if word in used_words:
            return [(i % n) + 1, (i // n) + 1]
        
        used_words.add(word)  # 단어를 사용한 것으로 표시
        last_word = word[-1]  # 현재 단어의 마지막 글자를 다음 단어의 시작 글자로 설정
    
    return [0, 0]  # 끝까지 규칙을 어기지 않으면 [0, 0] 반환