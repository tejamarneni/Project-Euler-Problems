import math

maxval = 999 * 999 #largest product of 2 three digit numbers
minval = 100 * 100 #smallest product of 2 three digit numbers

sumval = 0
pal = []

while maxval != minval:
    temp = maxval   #temporary variable to store largest number
    while maxval > 0:
        num = maxval % 10  #captures the remainder of the number
        sumval = sumval * 10 + num
        maxval = maxval // 10     #captures the quotient of the number
    maxval = temp   #value is stored back into the maxval
    if sumval == maxval:   #checks if the number is a palindrome
        for val in range(1,int(math.sqrt(maxval))):   #checks if the number is a composite number
            if maxval % val == 0:
                pal.append(maxval)   #appends the value into the list
                break   #breaks out of the if loop
        break     #breaks out of while loop
    maxval -= 1   #decreases the value of maxval by 1
    sumval = 0    #resets the sumval back to 0

print(pal)    