prime_list = []

def primelist(num):
    i = 0
    j = 3
    while i <= num:
        d = 0
        for k in range(3,int(j**0.5)+1,2):
            if j % k == 0:
                d += 1
        if d == 0:
            prime_list.append(j)
            i += 1
        j += 2
    return prime_list     

# prints n prime numbers
print(sum(primelist(2000000)))
         