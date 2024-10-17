t = int(input())

for _ in range(t):
    n = int(input())
    bottles = 0
    king = ''
    
    for _ in range(n):
        school, alcohol = input().split()
        alcohol = int(alcohol)
        
        if bottles < alcohol:
            bottles = alcohol
            king = school

    print(king)