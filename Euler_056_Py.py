#Ariel Tynan
#Euler Problem 056, Powerful digit sum, solved in Python
#Started and solved 7 March 2022

import math

#Splits numbers into digits and sums them
def sum_digits(n):
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)
    return sum

max = 0 #max sum of digits
for i in range(1,100): #from 1 to 1000
    for j in range(1,100):
        if sum_digits(pow(i,j)) > max:
            max = sum_digits(pow(i,j))
            #print(i,j,max)
print("Answer: ",max)
            
