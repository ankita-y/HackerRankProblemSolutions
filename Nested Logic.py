d1, m1, y1= map(int,input().split())
d2, m2, y2= map(int,input().split())

if d1<=d2 and m1<=m2 and y1<=y2:
    print(0)
elif m1==m2 and y1==y2:
    print(15*(d1-d2))
elif m1>m2 and y1 == y2:
    print(500*(m1-m2))
elif y1 > y2:
    print(10000)
else:
    print(0)

"""
23 12 1234
19 9 2468

24 12 1898
18 9 1898
"""