import re

if __name__ == '__main__':
    N = int(input())
    firstNameSort = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.findall("@gmail.com$",emailID):
            firstNameSort.append(firstName)

    firstNameSort.sort()
    for name in firstNameSort:
        print(name)
"""
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com"""






