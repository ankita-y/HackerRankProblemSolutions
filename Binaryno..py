if __name__ == '__main__':
    n = int(input())
    convert = bin(n)

    convert = convert[2:]

    print(max(map(len,convert.split('0'))))





