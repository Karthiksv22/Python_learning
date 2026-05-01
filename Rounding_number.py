import math
import random

# Rounding numbers
# We have to import the math lib because some function comes inside that 
price = 35.54820382
print(round(price))            # round up the value
print(round(price,2))
print(round(price,1))
print(math.floor(price))
print(math.ceil(price))
print(int(price))


#Random functions
# We have to import the random lib because some function comes inside that 

print(random.random())      # By doing this we will get random numbers

print(random.randint(1,10))              # By doing this we get random int number that is from 1 to 10


# Validating our numbers
# Using is_integer
x = 7.0
print(x.is_integer())

x = 7.2
print(x.is_integer())

#Using isinstance
x = 70.4
print(isinstance(x,int))
print(isinstance(x,float))


# Challence vedio time
# Generate random number from 1 to 100 and check whether it is even number

num = random.randint(1,100)

print("Generated num is ",num)

if num % 2 == 0:
    print("It is an even number")
else :
    print("It is odd number")





