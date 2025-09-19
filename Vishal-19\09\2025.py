def looping():
    a=int(input())
    k=int(input())
    added_value=a
    for i in range(k):
        if(str(add)==str(add)[::-1]):
            return i,add
        else:
            added_value=a+int(str(add)[::-1])
            a=added_value
print(looping()) 
