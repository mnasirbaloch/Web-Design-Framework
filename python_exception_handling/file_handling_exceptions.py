# FileNotFoundError - This exception is raised when a file or directory is not found.

# Example:
try:
    file = open("no_file.txt")
except:
    print("File not found exception"
          )
    


#UnsupportedOperation
#Exception which will be thrown when we try to perform a operation which is not allowed as,
try:
    file = open("introduction_to_execption.txt.txt","w") #we are opening file in write mode
    file.read() #exception will be thrown because we open file in write mode
except Exception as e:
    print(e)


