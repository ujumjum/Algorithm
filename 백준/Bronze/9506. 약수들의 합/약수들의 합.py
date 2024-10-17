while True:
    n = int(input())
    if n == -1:
        break
        
    divisors = []
    sum_divisors = 0
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            divisors.append(i)
            
            if i != 1 and i != n // i:
                sum_divisors += n // i
                divisors.append(n // i)
                
    if sum_divisors == n:
        print(f"{n} = {' + '.join(map(str, sorted(divisors)))}")
    else:
        print(f"{n} is NOT perfect.")