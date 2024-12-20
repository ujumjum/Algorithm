def solution(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:].lower())
        else:
            result.append('')
            
    return ' '.join(result)