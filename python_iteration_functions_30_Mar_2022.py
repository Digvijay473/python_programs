#var={'name':'dhoni','age':33}
#for x in var:  #it prints only keys
#    print(x)
#var={'name':'dhoni','age':33}
#for x in var.items(): #it prints keys as well as vales also
#    print(x)

#var={'name':'dhoni','age':33}
#for x in var.values():#it prints only values
#    print(x)


#-----------------------------

#when you want to print values from given dictionary in another list then below is example
#mylist=[]
#var={'name':'dhoni','age':33}
#for x in var.values():
#    mylist.append(x)
#print(mylist)   



#use of range()

#for x in range(10): #prints 0 to 9
#    print(x)

#for x in range(1,10): #prints 1 to 9
#    print(x)


#we want to put all even values between 1 to 10 in list

#option 1
#mylist=[]
#for x in range(10):
#    if x%2==0:
#        mylist.append(x)

#print(mylist)

#option 2

#mylist=[x for x in range(10) if x%2==0]
#print(mylist)

#tuple
#tuple is imutable
#tuple contain more than one values in only one value is there then we have to put coma to make it tuple class otherwise it remains a string class
#we can not change values because its imutable but we can add  tuples

#var=('a','b')
#print(type(var))

#var=('a','b')

#var[0]='hello' #we can not change values because its imutable
#print(var)

var=('a','b')
var1=('c','d')
print(var+var1)








