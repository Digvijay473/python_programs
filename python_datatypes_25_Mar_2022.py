#var={}
#print(var)
#print(type(var))





























#var={"name":'dhoni', 'age':33, 'name':'MSD'}#duplicate key not allowed
#print(var)#when you use duplcate key then it assign last value to the key

#keys are unique
#Dictionary is called Unordered collection
#var={'name':'dhoni', 'age':33, 9:('a','b'), True:'rj'}#keys can anything except list because list is mutable but we can insert list under key 
#print(var)

#var={"name":'dhoni', 'age':33, 'name':'MSD'}
#var1={99:33}
#var2={3:'ak', 2:'dk'}
#output=var+var1#we cant concatenate 2 dicionaries in 
#print(output)


var={'name':['dhoni','kohli'],'team':('csk','rcb'),'sports':{'cricket':['sachin','dravid']}}
#print(var)

output=var['name'][0]
print(output)

var['team'][0]='Msd'
print(var)










