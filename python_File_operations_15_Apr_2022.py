import csv
##with open('PythonFileoperaion.csv','w') as file_obj:
##    #file_obj_csv=csv.file_obj()#wrong method
##    file_obj_csv=csv.writer(file_obj)
##    file_obj_csv.writerowrow(['name','age','runs'])
##    file_obj_csv.writerows([['msd',40,32],['yuvi',40,82]])

##with open('Pyt.csv','w') as obj: #object created here
##    obj_csv=csv.writer(obj)  #here we are convrting into csv    
##    obj_csv.writerow(['name','age','runs']) #writerow()used to create heading that is column name only one row
##    obj_csv.writerows([['Diggy',40,32],['Akki',40,82]])#writerows()used to enter records(data) i.e list of lists
  
##with open('Python1.csv','w',newline='') as obj: #object created here and [newline=''] used to insert data row by row without giving any blankline  in between
##    obj_csv=csv.writer(obj)  #here we are convrting into csv    
##    obj_csv.writerow(['name','age','runs']) #writerow()used to create heading that is column name only one row
##    obj_csv.writerows([['Digvijay',25,97],['Varpe',25,87]])#writerows()used to enter records(data) i.e list of lists


##with open('Pythondict.csv','w',newline='') as obj: ##using dictionary
##    obj_csv=csv.DictWriter(obj,['name','age','runs'])#istead of writerow function we hav to in this formate for dictonary 
##    obj_csv.writeheader() #use writeheader() to create fist row in column as a heading of that column i.e ame of column
##    obj_csv.writerows([{'name':'Digvijay','age':25,'runs':97},{'name':'Varpe','age':25,'runs':87}])#writerows()used to enter records(data) i.e list of lists

##Using pandas 

##IMP
##Use of DataFrame= 2 dimensions
##Use of Series= single dimension
##Use of Panels= 3 dimentions
import pandas
input1=[['name','rollno','marks'],['digvijay',473,87],['akash',47,97],['diggy',25,68]]
input2=pandas.DataFrame(input1)
print(input2)
input2.to_csv('secondpandas.csv')
