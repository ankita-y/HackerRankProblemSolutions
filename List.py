if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        s = input().split()
        cmd = s[0]
        a = s[1:]
        if cmd == 'insert':
            l.insert(int(a[0]),int(a[1]))
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'append':
            l.append(int(a[0]))
        elif cmd == 'print':
            print(l)
        elif cmd == 'reverse':
            l.reverse()
        elif cmd == 'remove':
            l.remove(int(a[0]))
        elif cmd == 'pop':
            l.sort()