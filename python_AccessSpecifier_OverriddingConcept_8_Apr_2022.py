##
##class myclass:
##    def __init__(s,name,age):
##        s.name=name
##        s.age=age
##        
##
##    def one(s):
##        print("First Function ",s.name)
##
##
##class second(myclass):#inherit myclass(parent) from second(child)
##    def two(s):
##        print("First Function ",s.name,s.age)
##
##my=second('yuvi',12)
##my.one()
##my.two()


##class myclass:
##    def __init__(s,name,age):
##        s.name=name
##        s.age=age
##        
##
##    def one(s):
##        print("First Function ",s.name)
##
##
##class second(myclass):
##    def two(s):
##        print("First Function ",s.name,s.age)
##
##my=second('yuvi',12)
##my.one()#accessing function of parent class (myclass) from child class(second)
##myparent=myclass('yuvi',12)
##my.two()#accessing function of child class(second) from parent class (myclass)

###Multiple Inheretance

class A: #parent class

    def fun(s):
        print("This is class A")

class B(A): #child class of A
    pass
    def fun(s):
        print("This is class B")

class C(A): #child class of A
    def fun(s):
        print("This is class C")

class D(B,C):#child class of B and C
    pass
        #def fun(s):
    
        #print("This is class D")
my=D()
my.fun()

#method Resolution order
#Near by search

##**1. In above example if we run the program without pass keyword at line number 57 then the output is "This is class D"
    ##**1.1. There are must be one statement after ":" and if we dont want to execute statement then simply put pass keyword then its  move to next executable statement
##**2. if we use pass keyword in D class at line number 57 then its take next executable statement that is in class B so the ouput is "This is class B"
    ##**2.1. its take class B because "class D(B,C):" inherit class B before class C
##**3. if the "class D(C,B):" then it will gives output as a "This is class C"
    ##**3.1. another way to achieve "This is class C" this output is put pass keyword in line number 48  when class D(B,C):


