#first way
append_list=[1,2,3,4,5,'avinash','singh']
append_list.append(9)
append_list.append('raja')
print(append_list)

#second way

list = []
def function(x,y,z):
      list.append(x)
      list.append(y)
      list.append(z)
function(1,2,3)
print(list)

#third way
l=[]
def userinput(*arg):
    l.append(arg)
final=userinput(7,4,1,2,5,8,9,6,3)
print(l)
