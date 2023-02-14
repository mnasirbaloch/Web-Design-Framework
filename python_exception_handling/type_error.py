#Type error
#Type error can be thrown in various cases such as,
    #Performing mathematical operation on non-numberic type




#Example 01
var1 = 45
var2 = "Nasir"
#lets use try catch
try:
    var3 = var1 + var2
except TypeError as e:
    print("Exception:",e)





#Example 02
#Comparing non-relative data types
var1 = 34
var2 = "Nasir"
#print(var1>var2)       #it will generate error because string and int are non-compareable
try:
    print(var1>var2)
except TypeError as e:
    print(e)




#Example03 
#Calling a function with wrong argument
def sum(va1,var2):
    sum = 0
    try:
       sum= var1 + var2
    except TypeError as e:
        print(e)
#If above function invoked with argument other than number the line
#var1+var2 will through exception so we handled it in try catch

sum(45,"")