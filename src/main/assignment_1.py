# 6 questions

import math #importing required for truncate function

#1
#Use double precision to calculate the resulting values(format to 5 decimal places)
# 0 10000000111 111010111001 

#-1^s * 2^(c-1023) * (1 + f)

def double_precision(s, c, f): #function to find the value of the specified string of binary code

    i = 0 #creating variable to loop through the string of binary code for the exponent
    c = str(c) #converting the binary code line to a string
    exponent_part = 0 #creating the variable where the exponent value will be stored

    while (i<11): #looping through each element in the string and adding the appropriate value
        exponent_part += int(c[i])*2**(10-i) #keeping un-rounded value
        i += 1

    j = 0 #creating variable to loop through the string of binary code for the fractional part
    f = str(f) #converting binary code line to a string
    fractional_part: float = 0.0 #creating the variable where the fractional value will be stored

    while (j<12): #looping through each element in the string and adding the appropriate value
        fractional_part += int(f[j])*(.5)**(j+1) #adding un-rounded value
        j+=1

    value = (-1)**s * 2**(int(exponent_part) - 1023) * (1 + fractional_part) #calculating the double precision value

    return value #returning said value

s_binary: str = 0 #splitting the binary line into the appropriate sections
c_binary: str = 10000000111
f_binary: str = 111010111001


number_one = double_precision(s_binary, c_binary, f_binary) #calling the function to calculate the double precision value from the binary line

print(format(number_one, '.5f')) #printing the answer to number one, to 5 decimal places


#2
#Repeat number 1 using three-digit CHOPPING arithmetic


def chopping_values(s, c, f):
    i = 0 #creating variable to loop through the string of binary code for the exponent
    c = str(c) #converting the binary code line to a string
    exponent_part = 0 #creating the variable where the exponent value will be stored

    while (i<11): #looping through each element in the string and adding the appropriate value
        exponent_part += math.trunc(int(c[i])*2**(10-i)*1000)/1000 #cutting all decimals off after the 3rd decimal
        i += 1

    j = 0 #creating variable to loop through the string of binary code for the fractional part
    f = str(f) #converting binary code line to a string
    fractional_part: float = 0.0 #creating the variable where the fractional value will be stored

    while (j<12): #looping through each element in the string and adding the appropriate value
        fractional_part += math.trunc(int(f[j])*(.5)**(j+1)*1000)/1000 #cutting all decimals off after the 3rd decimal
        j+=1

    value = (-1)**s * 2**(int(exponent_part) - 1023) * (1 + fractional_part) #calculating the double precision value

    return value #returning said value
    
number_two = chopping_values(s_binary, c_binary, f_binary) #calling function to calculate using chopped variables

print(format(number_two, '.5f')) #printing the answer to number 2

#3
#Repeat number 1 using three-digit ROUNDING arithmetic

def rounding_values(s, c, f): #function to find the value of the specified string of binary code

    i = 0 #creating variable to loop through the string of binary code for the exponent
    c = str(c) #converting the binary code line to a string
    exponent_part = 0 #creating the variable where the exponent value will be stored

    while (i<11): #looping through each element in the string and adding the appropriate value
        exponent_part += round(int(c[i])*2**(10-i), 3) #rounding to 3 digits and adding
        i += 1

    j = 0 #creating variable to loop through the string of binary code for the fractional part
    f = str(f) #converting binary code line to a string
    fractional_part: float = 0.0 #creating the variable where the fractional value will be stored

    while (j<12): #looping through each element in the string and adding the appropriate value
        fractional_part += round(int(f[j])*(.5)**(j+1), 3) #rounding to 3 digits and adding
        j+=1

    value = (-1)**s * 2**(int(exponent_part) - 1023) * (1 + fractional_part) #calculating the double precision value

    return value #returning said value

number_three = rounding_values(s_binary, c_binary, f_binary) #calculating using rounding to 3 digits

print(format(number_three, '.5f')) #printing the answer to number 3

#4
#Compute the absolute and relative error with the exact value from question 1 and its 3 digit ROUNDING

def absolute_error(exact, rounded): #function to calculate the percentage of absolute error
    difference = abs(exact - rounded) #calculate difference
    print(round(difference*100,5)) #express as a percentage

absolute_error(number_one, number_three)

def relative_error(exact, rounded): #function to calculate the percentage of absolute error
    difference = abs(exact - rounded) #calculate the difference
    relativity = difference/abs(exact) #divide the difference by the exact calculated value
    print(round(relativity*100, 5)) #express as a percentage

relative_error(number_one, number_three)

#5
#Consider the infinite series
# f(x)= SUM(k=1,inf)[{(-1)^k}({x^k}/{k^3})]
#What is the minimum number of terms needed to compute f(1) with error < 10^-4

def check_alternating(function):
    if "-1**k" in function:
        return True
    else:
        return False

def check_always_decreasing(function):
    check = True
    k = 1
    starting_value = abs(eval(function))

    for k in range(2, 5):
        result = abs(eval(function))

        if starting_value <= result:
            check = False
    
    return check


function = "(-1**k) * (x**k) / (k**3)"
x = int(1)
check1 = check_alternating(function)
check2 = check_always_decreasing(function)

if check1 and check2:
    number_of_terms = (10**(4/3))-1
    n = math.ceil(number_of_terms)
    print(n)



#6
#Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0
#with accuracy 10^-4 using a = -4 and b = 7.
#a) Using the bisection method


#b) Using the newton Raphson method

