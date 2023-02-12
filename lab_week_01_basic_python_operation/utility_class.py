#A class which contains the task of week 1 lab
class UtilityWeek1:
#Static methods are methods which don't require class instance and are accessed directly
#via class name as Utility.methodName()

#A method which will get an input from user and return Grade respectively
    @staticmethod
    def getGrade():
        print("Grade Calculator")
        # input returns a string we have to convert it in desired type, our desired type here is int
        marks = int(input("enter your marks to calculate grade:"))
        if(marks >= 80):
            print("You got grade A")
        elif (marks >=70):
            print("You got grade B")
        elif (marks>=60):
            print("yout got grade C")
        elif (marks>=50):
            print("you got grade D")
        else:
         print("You got grade F")

#A method which get 4 values from user and print the max value, we can use loop here as 
#well to get input from user and can store in different variables or even a list
    @staticmethod
    def getMax():
        print("Max Value Finder")
        var1 = int(input("Enter value 1:"))
        var2 = int(input("Enter value 2:"))
        var3 = int(input("Enter value 3:"))
        var4 = int(input("Enter value 4:"))
        print("maximum value from the given values {}, {}, {}, {}, is:{} ".format(var1,var2,var3,var4,max(var1,var2,var3,var4)))

#A method which will sort the provided list, here we are getting 4 values, storing in list
#and then sorting them
    @staticmethod
    def sortList():
        print("List Sorter")
        var1 = int(input("Enter value 1:"))
        var2 = int(input("Enter value 2:"))
        var3 = int(input("Enter value 3:"))
        var4 = int(input("Enter value 4:"))
        myList = [var1,var2,var3,var4]
        myList.sort()
        print(myList)


#A method which will return fail in case any of given value is less than 33 or
# the average of all numbers is less than 44 otherwise
#return pass
    @staticmethod
    def getFailPass():
        print("Pass/Fail Checker")
        var1 = int(input("Enter value 1:"))
        var2 = int(input("Enter value 2:"))
        var3 = int(input("Enter value 3:"))
        if(var1<33 or var2<33 or var3<33):
            print("you are failed because you have less than 33 marks")
        elif(((var1+var2+var3)/3)<40):
            print("You average is less than 40, you are fail")
        else:
            print("Congratulation you are pass")


#a method which will check if the provided item is in a list or not, here we are using
#predefined list, we can take values in list from user as well.
    @staticmethod
    def findElementInList():
        print("Find Item From List")
        myList = ["Nasir","Sabir","Asghar","Amjad","GM","Rehan Faheen","Salman"]
        name = input("Enter your name to find in list:")

        # using try catch, because index() throw error if element is not in list
        #so we handle that and show a message to user that element is not in list
        try:
           index = myList.index(name)
           print("Name exist in index:{}".format(index))
        except:
            print("Name is not in list")
