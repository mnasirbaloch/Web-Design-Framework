#ZeroDivisionError is thrown when we divide a number by zero
var1 = 45
try:
    45/0 #will thow ZeroDivisionError
except ZeroDivisionError as e:
    print(e)





#NameError #Error which is thorwn when non-declared variable is used
try:
    print(z) #will throw error as z is not declared
except NameError as e:
    print(e)





#IndexError - This exception is raised when you try to access an element 
# in a sequence using an index that is out of range.
list = [1,2,3,4]
try:
    list[8] #will throw IndexError as index 8 is not in list
except IndexError as e:
    print("Index out of bound error")




# KeyError - This exception is raised when you try to access a non-existent key in a dictionary.
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"]) #will throw excpetion of KeyError as c is not a key in our dict
except:
    print("Key not found in dictionary")


# AttributeError - This exception is raised when you try to access an attribute that does not exist.
#This is same as accessing a method which does not exist in object class
my_str = "hello"
try:
    my_str.foo() #will generate error as foo is not a method of string list
except  ArithmeticError as e:
    print("Exception: ",e)


