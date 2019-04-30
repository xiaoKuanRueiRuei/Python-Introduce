import sys
sys.setrecursionlimit(2000)
#支援大數據
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)