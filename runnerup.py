#minion game
if __name__ == '__main__':
    string = input()
    vowel = 'AEIOU'
    s = 0
    k = 0
    for i in len(string):
        if string[i] in vowel:
            k += len(string) - i
        else:
            s += len(string) - i

    if k > s:
        print("k",k)
    elif k < s:
        print("S",s)
    else:
        print("Draw")