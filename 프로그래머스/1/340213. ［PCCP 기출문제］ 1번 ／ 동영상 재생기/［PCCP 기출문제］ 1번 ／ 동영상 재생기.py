def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time):
        m, s = map(int, time.split(":"))
        return m*60 + s
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    if op_start <= pos <= op_end :
        pos = op_end
        
    for command in commands:
        if command == "prev":
            pos = max(0, pos-10)
        elif command == "next":
            pos = min(video_len, pos+10)
        
        if op_start <= pos <= op_end:
            pos = op_end
    
    m = pos // 60
    s = pos % 60
    
    return f"{m:02d}:{s:02d}"