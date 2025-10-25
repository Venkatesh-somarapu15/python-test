list=[]
a=int(input("enter the list of elements"))
for i in range(1,a+1):
    value=int(input("enter value:"))
    list.append(value)
list.sort()
print("the  second largest number",list[a-2])
 