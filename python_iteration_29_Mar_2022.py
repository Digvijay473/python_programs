#data='india is my country' #it gives all letter on new line
#for x in data:
#    print(x)

#data='india is my country'
#for x in data:
#    print(x,end=' ')#for put in one line 


#data='india is my country'
#for x in enumerate(data):
#    print(x)#it gives index as well as all letters

    
#data='india is my country'
#for x, y in enumerate(data):
#    print(x, end='')#indicates letters
#    print(y, end=' ')#indicates indexes

#data='india is my country'#if we want to print length without using len()
#count=0
#for x in data:
#    count=count+1
#    print(count)#it gives count one by one
    
#data='india is my country'#if we want to print length without using len()
#count=0
#for x in data:
#    count=count+1
#print(count)#it gives final count

#data='india is my country'#use of if loop
#for x in data:
#    if x=='i':              #we are giving condition that letter is i
#        print(x,'success')  # if letter is i its print success
#    elif x=='c':
#        print(x,'success')   # if letter is c its print success
        
#    else:
#        print(x,'failure')  # if letter is other than i and c its print failure


#data='India is my country'#using or instead of elif
#for x in data:
#    if x=='i' or x=='c':
#       print(x,'success')
#    else:
#        print(x,'failure')

#data='India is my country'#using or instead of elif
#for x in data:
#    if x=='i' or x=='c':
#        print(x,'success')
#        break            #it prints till condition get satisfied and breaks the loop when condition gets satisfied
#    else:
#        print(x,'failure')


data='India is my country'#using or instead of elif
for x in data:
    if x=='i' or x=='c':
        print(x,'success')  #continue is opposite of break
        break           #it prints  condition till get satisfied and continue the loop when condition gets satisfied
    else:
        print(x,'failure')




