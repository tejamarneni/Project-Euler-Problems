n1 = 1
n2 = 2
sumval = 0
l =[n1]
n = int(input("Enter the number that you want to add upto:\n")) #user input for the sum in the fibonacci series

while sumval <= n:
    l.append(n2) #appends each elements to the list from the fibonacci series
    sumval = n1 + n2 
    n1 = n2
    n2 = sumval

s = 0

for num in l:
    if num % 2 == 0:
        s = s + num #Add even numbers

print(f"The sum of even numbers upto {n} in the list is " + str(s))
print(l) #prints the list of the series
print(n1)   #prints the last number in the list