# 6 questions
# testing


#1
#Use double precision to calculate the resulting values(format to 5 decimal places)
# 0 10000000111 111010111001 

#-1^s * 2^(c-1023) * (1 + f)

def double_precision(s, c, f): #function to find the value of the specified string of binary code

    i = 0 #creating variable to loop through the string of binary code for the exponent
    c = str(c) #converting the binary code line to a string
    exponent_part = 0 #creating the variable where the exponent value will be stored

    while (i<11): #looping through each element in the string and adding the appropriate value
        exponent_part += int(c[i])*2**(10-i)
        i += 1

    j = 0 #creating variable to loop through the string of binary code for the fractional part
    f = str(f) #converting binary code line to a string
    fractional_part: float = 0.0 #creating the variable where the fractional value will be stored

    while (j<12): #looping through each element in the string and adding the appropriate value
        fractional_part += int(f[j])*(.5)**(j+1)
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
        exponent_part += int(c[i])*2**(10-i)
        i += 1

    j = 0 #creating variable to loop through the string of binary code for the fractional part
    f = str(f) #converting binary code line to a string
    fractional_part: float = 0.0 #creating the variable where the fractional value will be stored

    while (j<12): #looping through each element in the string and adding the appropriate value
        fractional_part += format(int(f[j])*(.5)**(j+1),'.3f')
        j+=1

    value = (-1)**s * 2**(int(exponent_part) - 1023) * (1 + fractional_part) #calculating the double precision value

    return value #returning said value
    


#3
#Repeat number 1 using three-digit ROUNDING arithmetic


#4
#Compute the absolute and relative error with the exact value from question 1 and its 3 digit ROUNDING


#5
#Consider the infinite series
# f(x)= SUM(k=1,inf)[{(-1)^k}({x^k}/{k^3})]
#What is the minimum number of terms needed to compute f(1) with error < 10^-4


#6
#Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0
#with accuracy 10^-4 using a = -4 and b = 7.
#a) Using the bisection method


#b) Using the newton Raphson method

