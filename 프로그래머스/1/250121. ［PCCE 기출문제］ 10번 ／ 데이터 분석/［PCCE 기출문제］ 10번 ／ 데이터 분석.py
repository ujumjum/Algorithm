def solution(data, ext, val_ext, sort_by):
    # 인덱스화
    idx = {
        "code" : 0,
        "date" : 1, 
        "maximum" : 2, 
        "remain" : 3,
    }
    
    answer = []
    
    for row in data:
        if row[idx[ext]] < val_ext:
            answer.append(row)
            
    answer.sort(key=lambda x : x[idx[sort_by]])
    
    return answer