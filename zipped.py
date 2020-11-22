if __name__ == '__main__':
    n, x = map(int,input().split())
    grade = list()
    for i in range(x):
        row = list(map(float,input().split()))
        grade.append(row)
    #used zipped to bind the element from array
    print(*[sum(i)/x for i in zip(*grade)],end='\n')


    """ average = [sum(i)/x for i in zip(*grade)]
    for i in average:
        print(i)"""
    """
    Testcases
    5 3
    89 90 78 93 80
    90 91 85 88 86  
    91 92 83 89 90.5
    
    """

