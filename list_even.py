def check(x):
    if(x % 2 == 0 or x % 4 == 0):
        return 1
evens=list(filter(check, range(2,22)))
print(evens)

def checkkrbhai(num):
    if(num % 2 ==0 or num % 4 ==0):
        return 1
number=list(filter(checkkrbhai, range(2,70)))
print(number)
