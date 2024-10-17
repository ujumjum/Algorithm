operations = {
    '@': lambda x: x*3,
    '%': lambda x: x+5,
    '#': lambda x: x-7,
}

n = int(input())
for _ in range(n):
    expr = input().split()
    value = float(expr[0])
    
    for op in expr[1:]:
        value = operations[op](value)
    
    print(f"{value:.2f}")