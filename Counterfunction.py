#1. to calculate no of duplicate element in list
list1 = [1,2,4,6,2,1,1,3,7,7,9,9,6,8,6,1,3,2]
d = dict()
for i in list1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
#2.
list1 = [1,2,4,6,2,1,1,3,7,7,9,9,6,8,6,1,3,2]
d ={}
for i in list1:
    d[i] = list1.count(i)
    
print(d)
