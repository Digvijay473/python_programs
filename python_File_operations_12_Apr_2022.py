file=open("PythonFileOperation.txt","w")  #it will create new file in current folder that you are working
file.write("This is first python file opration")
file.close() # its necessary to close the file

###when we use operation "w" it will create new file and override the conetent of file if file already exist

##
##file=open("D:\Python_file_operations\PythonFileOperation.txt","w")  #it will create new file in folder that you are specified and it override first file content
##file.write("This is Second python file opration")
##file.close() # its necessary to close the file

##
##file=open("D:\Python_file_operations\PythonFileOperation.txt","a")#it will append existing file and write content without overriding
##file.write("\n")# to  write content on new line in existing file
##file.write("Welcome to python file opration")
##file.close() # its necessary to close the file


##file=open("PythonFileOperation.txt","a")#it will append existing file and write content without overriding
##file.write("\n")# to  write content on new line in existing file
##file_content=input("enter file content") #enter content dynamically(runtime)
##file.write(file_content)
##file.close() # its necessary to close the file

##file=open("PythonFileOperation.txt","x")#it will throw error that file already exist(File exists: 'PythonFileOperation.txt')
##                                        #when we use x it create new files only
##file.write("\n")# to  write content on new line in existing file
##file_content=input("enter file content") #enter content dynamically(runtime)
##file.write(file_content)
##file.close() # its necessary to close the file



##Context Manager
##with open("PythonFileOperation.txt","a") as file:
##    file.write("\n")
##    file_content=input("enter file content") 
##    file.write(file_content) #you not need to  close the file it automatically getting closed

##with open("PythonFileOperation.txt","r") as file:
##    file_op=file.read() #it print all the content of file
##    print(file_op)
##
##with open("PythonFileOperation.txt","r") as file:
##    file_op=file.read(5)# it prints first 5 characters
##    print(file_op)
##    file_op1=file.read()# it prints all the data after first 5 characters
##    print(file_op1)

with open("PythonFileOperation.txt","r") as file:
    file_op=file.readline()# it prints first line(readline() reads only one line)
    print(file_op)
    file_op1=file.readline()# it prints second line(line after first because cursor points at end of first line[file_op=file.readline()] )
    print(file_op1)
               




