#The Python ValueError is an exception that occurs when a function 
#receives an argument of the correct data type but an inappropriate value. 

#Example

import math


try:
    var1 = int("Hello") 
except ValueError as e:
    print(e)

#In try block int function receive correct type which is string
#but the value in string contains characters which are not allowed, only digits
#allowed, so here ValueError will be thrown which we handled using try-catch



#Example 02
myList = [1,2,3]
try:
    myList.remove(5) #will through ValueError that x not in list
except ValueError as e:
    print(e)



#Math Domain Error

value = -1
try:
    result = math.sqrt(value) #throw ValueError as square root of -1 is not in domain
except ValueError as e:
    print(e) 
