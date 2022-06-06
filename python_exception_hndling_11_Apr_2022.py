##var=10/0
##print(var) # it throws error that division by zero
##print("welcome")


##try:
##    var=10/0
##    print(var)
##
##except:
##    print("sorry")
##
##print("welcome")


try:
    var="a"+10
    print(var)

except: #default exception block
    print('sorry')

print('welocome')




##try :   #one try block having multiple except block
##    var =10/0
##    print(var)

##except TypeError:
##    print("sorry try again")

##except ZeroDivisionError:
##    print("sorry for the error")

##except: #default exception block
##    print("Sorry")
    

##try :   
##    var =10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as s: #you can write in single line with paranthesis also
##    print(s)
##
##except: #default exception block and it should be always last
##    print("Sorry")

##try :   
##    var =10/0
##    print(var)
##except Exception as s: #you can write in single line with Exception class
##    print(s)# here s is variable of xception class
##
##except: #default exception block and it should be always last
##    print("Sorry")

##try :   
##    var =10/4
##    print(var)
##except Exception as s: #this block excecute only if exception is raised
##    print(s)
##else: #this block excecute only if exception is not raised
##    print("this is else block")
##finally:#this block excecute in both cases where exception is raised or not
##    print("This is finally block")

##except: #default exception block and it should be always last
##    print("Sorry")





###User define Exception
##
##var=10
##try:
##    if var>5:
##
##        raise IndexError()
##except IndexError:
##    print("this is user define exception")



##var=10
##try:
##    if var>5:
##
##        raise IndexError()
##except IndexError as s: #it gives you blank output you cant use this in userdefine exception
##    print(s)


##var=10
##try:
##    if var>5:
##
##        raise IndexError("this is user define exception")#you can print like this
##except IndexError as x:
##    print(x)


##class netzwerk(Exception):
##    myerror="user define exception"
##var=10
##try:
##    if var>5:
##
##        raise netzwerk()
##except netzwerk: 
##    print('sorry')

##class Netzwerk_Error(Exception):
##    myerror="user define exception"
##var=10
##try:
##    if var>5:
##
##        raise Netzwerk_Error()
##except Netzwerk_Error as ex: # you can use this because you are derived class Exception by Netzwerk_Error
##    print(ex.myerror)















    





    


    
