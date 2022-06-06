#string, list, tuple and dictionary, numbers
#set and frozenset

#1. Mutable --- list and dictionary--(you can modify object using index number)
#2. Immutable ---string, tuple, numbers--(you can not modify object using index number)

data="netzwerk"
data='academy' # it will override first data
print(data)
print(type(data))
####
####Data='academy'
####print(Data)
####print(type(Data))
####
####

##we  can concatenate 2 strings as follows
##Data='academy'
##data="netzwerk"
##Sum= Data+data
##print(Sum)
##print(type(Sum))

###OR
##Data='academy'
##sum=Data+' Netzwerk'
##print(sum)
##print(type(sum))

##OR
##sum='netzwerk'+' \n academy' # \n prints data on new line 
##print(sum)
##print(type(sum))

#using of tripple quote---(when we want to print multiple rows/lines in single print function)

##language='''this is programming language
##and i love this language'''
##print(language)
##
##print('''this is python
##      language''') #it will print the data inside the tripple quote in multiple lines

#use of slash(\)--- #it will print the data inside the tripple quote in single line

##country='''India is my country \
##and I love my country'''
##print(country)

name='dhoni'
age=33

#Indian captian playes even at the age of

##MS="Indian captian %s playes even at the age of %d"%(name,age)
##print(MS)




#Another way by separating strings

MSD="Indian captian " +name+ " playes even at the age of " +str(age)
print(MSD);

#Another way by using f before string

#MSDCOOL=f"Indian captian {name} playes even at the age of {age}"
#print(MSDCOOL)

#Another way by using format after string

##MSDFAN='Indian captian{} playes even at the age of{}'.format(name,age)
##print(MSDFAN)
