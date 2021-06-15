# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.
# 1
k = int(input())
rooms = list(map(int,input().split()))
single, multiple = set(), set()

for room in rooms: single.add(room) if room not in single else multiple.add(room)

print(single.difference(multiple).pop())

# 2
target = int(input())
s = list(map(int,input().split()))

d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key,val in d.items():
    if d[key] != target:
        print(key)
