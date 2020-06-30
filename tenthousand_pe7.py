def primenums(nums):
    primelist = []
    x = 3
    while len(primelist) < nums:
        if all([x % prime for prime in primelist]): #loops through list of prime numbes.
            primelist.append(x)
        x += 2
    print(primelist)        

primenums(10001)