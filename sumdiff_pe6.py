def sumdif(num):
    squaresum = 0
    sumsquare = 0
    for i in range(1,num+1,1):
        sumsquare += i
        i = i * i
        squaresum += i
    sumsquare = sumsquare * sumsquare    
    diff = sumsquare - squaresum
    return print(diff)

sumdif(100)       
