

if __name__ == '__main__':

    n = int(input())
    phone_dict = dict()
    for i in range(n):
        row = input().split()
        phone_dict[row[0]] = int(row[1])

    while True:
        try:
            name = input()
            if name in phone_dict:
                print("{}={}".format(name, phone_dict[name]))
            else:
                print("Not Found")
        except EOFError as e:
            break



    """for i in range(n):
        name = input()
        if name in phone_dict:
            print("{}={}".format(name,phone_dict[name]))
        else:
            print("Not Found")
    print(phone_dict)"""
