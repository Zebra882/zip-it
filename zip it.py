list1={1,2,3}
list2={1,2,3,4,5}
list3=list(zip(list1,list2))
print(list3)

list1={'a','b','c','d'}
list2={1,2,3,4,5}
list3=list(zip(list1,list2))
print(list3)

lst1=[11,35,10,66]
lst2=[146,545,184,153]
for x,y in zip(lst1, lst2[::-1]):
    print(x,y)
    
