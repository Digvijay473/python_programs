##python is unstructured programming
##python is made as structured programming if its follows class principles
##class is collection of object
##object is real world entity
##class is kind of template or wrapper to hold the things
##object is anything which take memory
##class is mainlytogive property of inheritance or extensibility

##name='yuvi'
##print(name)
##
##def fun():
##    print('welcome')
##fun()

##class Myclass:
##    name='yuvi'
##
##    def fun():
##        print('welcome')
##Myclass.fun()
##print(Myclass.name)

    
class myclass:
    name='yuvi'

    def fun():
        print('welcome')

print(myclass.name)
myclass.fun()

my=myclass#my is called object reeference of myclass
print(my.name)
my.fun()


###Class Without Constructor

##class myclass:
##    
##    def fun1(name):
##        print('hello')
##        print(name)
##
##    def fun2(name,age):
##        print('welcome')
##        print(name,age)
##my=myclass
##my.fun2('yuvi',12)
##my.fun1('dhoni')

###Class With Constructor

### Constructor :- constructor shuold be same name of class name

    
##class myclass:
##
##    def __init__(s,name,age):
##        s.name=name
##        s.age=age
##        
##    def fun1(s):
##        print('hello')
##        print(s.name)
##        my.fun2()
##
##    def fun2(s):
##        print('welcome')
##        print(s.name,s.age)
##        
##my=myclass('yuvi',12)#here myclass is called as constructor of class
##my.fun2()
##my.fun1()

##my is the object reference with single instant memory
##whenever you create a constructor an attribute __init__ is created automatically
##we can use that __init__ if we need to initialize the data inside the class
##attribute or magic method or dunder method is anything that contain double underscore on either side
##here we declare(s,name,age) s is similar my
##my is the object reference for external class
##self is the object reference for internal class



