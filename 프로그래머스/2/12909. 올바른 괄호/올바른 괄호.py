def solution(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0