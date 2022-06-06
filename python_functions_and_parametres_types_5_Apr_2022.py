##def Student_Passed(*names): #*args:- it can take multiple arguments and gives output in form of tuple
##    print(names)
##
##Student_Passed("msd",'kohli')
##Student_Passed("msd",'kohli','yuvi')


##def Student_Passed(**names): #**args means data with keys and gives output in form of dictionary
##    print(names)
##
##Student_Passed(name="msd",age=40)
##Student_Passed(name='yuvi')

##def student(eng,math,sname):
##    total= eng + math
##    return #it returns None 
##print(student(91,87,'Rocky'))

##def student(eng,math,sname):
##    total= eng + math
##    return #it returns None 
##    print('Welcome')
##print(student(91,87,'Rocky'))

##def student(eng,math,sname):
##    total= eng + math
##    return total#it returns total 
##    print('Welcome')#its ot executed because return is the last statement in function 
##print(student(91,87,'Rocky'))


##def student(eng,math,sname):
##    total= eng + math
##    return total#it returns total 
##    print('Welcome')#its ot executed because return is the last statement in function 
##output=student(91,87,'Rocky')
##print(output)

##def student(eng,math,sname):
##    total= eng + math
##    return total,sname#it returns total and sname 
##    print('Welcome')#its ot executed because return is the last statement in function 
##output,output1=student(91,87,'Rocky')
##print(output)#its print only total(output)
##print(output1)#its print sname(output1)
##print(output,output1)


#Scoping

##var=100#outside variable
##def fun():
##    var=10#inside variable   o/p=10,100,100
##    print(var)
##print(var)
##fun()
##print(var)

# recursion avoid using if loop and return statement   
##count=0
##def fun():
##    global count
##    print('infinity',count)
##    count=count+1
##    if count==101:
##        return count
##    fun()
##fun()

# recursion avoid using while loop
##count=0
##def fun():
##    global count
##    print('infinity',count)
##    count=count+1
##    while count < 101:
##        fun()
##fun()
##
### recursion avoid using if loop

##count=0
##def fun():
##    global count
##    print('infinity',count)
##    count=count+1
##    if count < 101:
##        fun()
##fun()


