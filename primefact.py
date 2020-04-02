def primefactor(num):
    result = [] # list to capture all the factors of the number from user.
    if num > 2:    
        for i in range(2,int(num**0.5)+1): #checks the factors of the number from 2 to sqrt of the number.
            if num % i == 0:
                result.append(i)  # appends the divsor to the result list.
                j = num / i
                if i != j:  
                   result.append(int(j))     # appends the quotient to the result list.                  
        if result != []:   # checks if the list is not empty.
            result = sorted(result) # sorts the result list in ascending order.
            print(f"The factors of {num} are ",result)
            valsub = [] # list to capture all the prime factors of the number from user.
            for vals in result: #loops through each elements in the result list.
                d = 0 # variable to count the factors of each number in the result list.
                for div in range(2,int(vals**0.5)+1): # checks for the factors of each number in the result list.
                    if vals % div == 0:
                        d += 1
                if d == 0:
                    valsub.append(vals) # if d is zero the number does not have any factors (prime number).
            valsub = sorted(valsub)        
            print(f"The prime factors of {num} are:",valsub)
            print("The largest prime factor of",num,"is",valsub[-1]) 
            print("The smallest prime factor of",num,"is",valsub[0])
        else:
            print(num,"is a prime number")      
    elif num == 0 or num == 1: # checks if user input is 0 or 1.
        print(num, "is a neither a composite number nor a prime number")
    elif num == 2:
        print("2 is a even prime number")              
    elif num < 0:
        print("Please Enter a Valid number")  # prints the statement if user enters a negative number.
       

# example for testing the code
primefactor(105)           