##class myclass:
##    """Author : Digvijay, Date 7 April 2022 This class is for constuctor """ 
##    def __init__(s,name,age):
##        s.name=name
##        s.age=age
##        
##    def fun1(s):
##        print('hello')
##        print(s.name)
##        
##
##    def fun2(s,country):#we can pass other arguments also
##        print('welcome')
##        print(s.name,s.age,country)
##        
##my=myclass('yuvi',12)#here myclass is called as constructor of class
##my.fun2('india')
##my.fun1()
##print(my.__doc__)

##
##class myclass:
##    def fun(s):
##        print('welcome to pune')
##my=myclass()
##my.fun()


##class myclass(object):
##    def __init__(s):
##        print('hello students')
##    def fun(s):
##        print('welcome to pune')
##my=myclass()
##my.fun()

class myclass(object):
    def fun(s):
        print('welcome to pune')
my=myclass()
my.fun()

