if __name__ == '__main__':
    n = int(input())
    #i_str = list()
    for i in range(n):
        i_str = input()
        print(*["".join(i_str[::2]),"".join(i_str[1::2])])
        """
        for i in i_str:
            if i_str.index(i)%2 == 0:
                print(*("".join(i)))
        print(end=" ")
        for i in i_str:
            if i_str.index(i)%2 != 0:
                print(i,end="")
"""


        #i_str.append(input())

    """for i in i_str:
        print(i)
    print(i_str)"""