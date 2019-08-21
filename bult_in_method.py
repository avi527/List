#Length
#append
#insert
#remove
#pop
#del
#clear
#copy

thislist=[1,2,3,4,5,6,7,8,9,0]
find_len=len(thislist)
print(f"this list length {find_len}")
#append
thislist1=['a','b','c']
thislist1.append('d')
print(thislist1)

#insert
insert1=['avi','sud']
insert1.insert(2,'swt')
print(insert1)

#remove
insert1.remove('sud')
print(insert1)

#pop
do_pop=['ac','dc',5,7,'avinash']
do_pop.pop()
print(do_pop)

#del
do_del=['kj','hjgfg','iug',9,8]
del do_del[3]
print(do_del)

#cler
do_clear=[7,8,9,5,'gfg']
do_clear.clear()
print(do_clear)
do_clear.append('hiii')
print(do_clear)

#clear
do_clear=[5,7,8,9,'jdfhf']
do_clear.copy()
print(do_clear)
