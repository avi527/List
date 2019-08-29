def duplicateRemove(x):
    return list(dict.fromkeys(x))
mylist=duplicateRemove([1,1,2,3,4,4,5,5])
print(mylist)

#second way
dub_list=[1,1,2,3,4,4,5,5]
a=list(dict.fromkeys(dub_list))
print(a)
