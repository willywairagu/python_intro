import math
import numpy  

# 1. STRINGS
print("Hello world") # this is a string 

# string operations
message = "hello "
message_2 = "world"

# joining the two strings above
complete_message = message + "" + message_2
print(complete_message)

print(message[1])

# getting the size of a string
print("The size of message is: ", len(message))
print("The size of message_2 is: ", len(message_2))

# iterating through a string - you canb use a loop
for char in message:
    pass
    # print(char) # uncomment to test this loop


# 2. INTEGERS AND BASIC MATH OPERATIONS
# WE TALKING ABOUT WHOLE NUMBERS
x = 10 
y = 3

# addition
sum = x + y
print(sum)

# subtraction
diff = x - y
print("difference: ", diff)

# division
ratio = x/y
print("ratio: ", ratio)

# modulus
remainder = x%y
print("Remainder: ", remainder)

# quotient 
quot = x // y # this is called floor division
print("Quotient: ", quot)

# multiplication 
product = x * y
print("Multiplication: ", product)

# raising to power 
power = x ** y 
print("result: ", power)

# square root 
answer = math.sqrt(10)
print("square root: ", answer)



# 3. FLOAT
#  numbers with decimal places
pi = 3.142
pi_ratio = 22/7
print("pi contant: ", pi, numpy.round(pi_ratio, 2))
