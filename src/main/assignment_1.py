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

absolute_error(number_one, number_three) #calling funcation to calculate the absolute error

def relative_error(exact, rounded): #function to calculate the percentage of absolute error
    difference = abs(exact - rounded) #calculate the difference
    relativity = difference/abs(exact) #divide the difference by the exact calculated value
    print(round(relativity*100, 5)) #express as a percentage

relative_error(number_one, number_three) #calling the funciton to calculate the relative error

#5
#Consider the infinite series
# f(x)= SUM(k=1,inf)[{(-1)^k}({x^k}/{k^3})]
#What is the minimum number of terms needed to compute f(1) with error < 10^-4

def check_alternating(function):#function to check if the function is alternating
    if "-1**k" in function: #if it has the alternating piece, return True
        return True
    else: #otherwise return False
        return False

def check_always_decreasing(function): #function to check if the function is always decreasing
    check = True #set it to True by default
    k = 1 #set starting k value
    starting_value = abs(eval(function)) #set starting function value with x = 1

    for k in range(2, 5): #calculate the values when k ranges from 2 and beyond
        result = abs(eval(function))

        if starting_value <= result: #if any value is greater than the starting it is not always decreasing
            check = False #then return False
    
    return check #return True or False


function = "(-1**k) * (x**k) / (k**3)" #defining function
x = int(1) #setting x equal to 1
check1 = check_alternating(function) #calling the function to check if the function is alternating
check2 = check_always_decreasing(function) #calling function to check if it is always decreasing

if check1 and check2: #if it is always decreasing and alternating we can assume
    number_of_terms = (10**(4/3))-1
    number_five = math.ceil(number_of_terms) #round up to get the number of terms
    print(number_five) #print the answer to number five



#6
#Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0
#with accuracy 10^-4 using a = -4 and b = 7.
#a) Using the bisection method

def bisection(left, right, function): #function to calculate number of iterations using bisection
    x = left
    starting_left = eval(function) #calclating at the left bound
    x = right
    starting_right = eval(function) #calculating at the right bound

    if starting_right * starting_left >= 0: #if left and right are ever of the same sign, return
        print("a and b are not of opposite sign.")
        return

    tol = .0001 #the defined tolerance
    difference = right - left #difference between the bounds
    max_iterations = 30 #maximum number of iterations to meet tolerance
    i = 0 #defining the iteration counter

    while (difference >= tol and i<= max_iterations): #looping until reaching tolerance or max iterations
        i += 1 #adding to iteration counter

        mid_point = (left + right)/2 #calculating the mid point
        x = mid_point 
        evaluated_at_mid = eval(function) #calcuating the function at the midpoint

        if evaluated_at_mid == 0.0: #if the value at the midpoint is 0, break the loop
            break

        x = left
        evaluated_at_left = eval(function) #calculating value of function at the left bound

        if evaluated_at_mid > 0 and evaluated_at_left < 0:
            right = mid_point #set right to the mid point if requirements met
        elif evaluated_at_mid < 0 and evaluated_at_left > 0:
            right = mid_point #set right to the mid point if requirements met
        else:
            left = mid_point #for all other results, set the left to the midpoint
        
        difference = abs(right - left) #calculate the difference with the new left or right

    return i #return the number of iterations


a = -4 #setting the left bound
b = 7 #setting the right bound
function_b = "(x**3) + 4*(x**2) - 10" #defining the function
number_6a = bisection(a, b, function_b) #calling the function to calculate the number of iterations

print(number_6a) #printing the answer to number 6a

#b) Using the newton Raphson method



