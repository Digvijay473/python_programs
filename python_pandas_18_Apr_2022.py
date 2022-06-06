#import numpy


##x=[1,2,3]
##print(x)
##print(type(x))
##
##y=numpy.array([1,2,3])
##print(y)
##print(type(y))
##
##z=numpy.array([[1,2,3],[4,5,6]])
##print(z)
##print(type(z))
##
##a=numpy.array([1,2,3],ndmin=2)
##print(a)
##print(type(a))

##data=numpy.dtype(numpy.int32)
##print(data)
##data=numpy.dtype('i4')
##print(data)

##data=numpy.array([[8,6,4],[4,9,3]])
##print(data)
##print(data.shape)

##data=numpy.array([[8,6,4,2],[4,9,3,7]])
##print(data)
##print(data.shape)
##data1=data.reshape(4,2)
##print(data1)
##print(data1.shape)

##data = numpy.empty([3,2],dtype=int)
##print(data)

##data = numpy.zeros(5)
##print(data)

##data=numpy.zeros((2,2),dtype=int)
##print(data)

##data=numpy.zeros((3,4),dtype=numpy.int32)
##print(data)

##data=numpy.zeros((3,4),dtype='i4')
##print(data)

#### broadcasting

##data=numpy.array([2,3,4,5])   
##data1=numpy.array([10,20,30,40])
##print(data*data1)

##data=numpy.array([[2,3,4,5],[1,2,3,4]])
##data1=numpy.array([10,20,30,40])
##print(data*data1)

import pandas
var=[[2,4,6],[2,1,3],[1,3,4]]
data=pandas.Series(var)
print(data)
##print(data.sum())
##print(data.prod())
print(data.max())
print(data.min())




