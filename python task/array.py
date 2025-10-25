#array1
from array import*
vals=array('i',[5,6,4,9,4])
print(vals)
#array2
from array import*
vals=array('i',[5,4,3,-9,5])
print(vals)
#array3
from array import*
vals=array('i',[5,4,3,-9,5])
print(vals.buffer_info())#buffer_info function shows address and size of the vals.
#array4
from array import*
vals=array('i',[5,4,-9,5])
print(vals.count(5))
#array5
from array import*
vals=array('i',[5,4,-9,5])
for e in vals:
    print(e)
#array6
from array import*
vals=array('i',[5,4,-9,5])
print(vals.index(-9))
#array6
from array import*
vals=array('u',['a','b','c'])
for w in vals:
    print(w)
#array7
from numpy import *
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)
arr=array([1,2,3,4,5],float)
print(arr)
from numpy import *
arr=linspace(1,2,3,4,5)
print(arr)