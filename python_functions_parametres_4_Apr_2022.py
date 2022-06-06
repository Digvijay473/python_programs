
##print ("hello")
##print("welcome to myfunction")

##def myfun():#function defination without pasing arguments
##        print ("hello")
##        print("welcome to myfunction")
##
###function call
##myfun()


##def myfun(name,country):#function defination with pasing arguments
##        print ("hello",name,"welcome to",country)
##        print("welcome to myfunction")
##
###function call
##myfun('virat','india')

##def myfun(name):#function defination with pasing arguments
##        print ("hello",name)
##        print("welcome to myfunction")
##
###function call
##myfun('virat')
##myfun('dhoni')
##myfun(1)# the numeric value is accepted


##def myfun(name):#function defination with pasing arguments and validaion
##    if isinstance(name,str):#we are giving the validation that only string is accepted
##        print ("hello",name)
##        print("welcome to myfunction")
##
###function call
##myfun('virat')
##myfun('dhoni')
##myfun(1)# the numeric value is not accepted


def myfun(name,country):#function defination with pasing arguments and validaion
    if isinstance(name,str): #we are giving the validation for name that only string is accepted
          if isinstance(name,str): #we are giving the validation for name that only string is accepted
                print ("hello",name,"welcometo",country)
                print("welcome to myfunction")

#function call
myfun('virat','india')
myfun('dhoni','india')
myfun(1,4)# the numeric value is not accepted


##def myfun(name,country):#function defination with default argument or signature or parameter
##    print ("hello",name,"from",country)
##    print("welcome to myfunction")
##
##myfun("kohli",'india')
##myfun('rocky','india')




##def myfun(name,country="austrelia"):#function defination with default argument or signature or parameter
##    print ("hello",name,"from",country)
##    print("welcome to myfunction")
####function Calling
##myfun("kohli")#when we pass only name value then it will take default value for country which we passes in function defination
##myfun('rocky','india')

##def myfun(name='rocky',country="austrelia"):##we can make both aruments as a default or only second argument as default but we cant make only first argument as a default 
##    print ("hello",name,"from",country)
##    print("welcome to myfunction")
####function Calling
##myfun()    
##myfun("kohli")
##myfun('rocky','india')


##def myfun(name='rocky',country):# it will trows error that we cant pass non default argument after default argument
##    print ("hello",name,"from",country)
##    print("welcome to myfunction")
####function Calling
##myfun()    #
##myfun("kohli")
##myfun('rocky','india')
