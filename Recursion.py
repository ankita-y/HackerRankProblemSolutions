if __name__ =='__main__':
    def factorial(n):
        #fact = 1
        if n <= 1:
            return 1
        else:
            fact = n * factorial(n-1)
            return fact


    n = int(input())
    result = factorial(n)
    print(result)