
import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    while not sum1==sum2==sum3:
        if sum1==max(sum1,sum2,sum3):
            x=h1.pop(0)
            sum1=sum1-x
        elif sum2==max(sum1,sum2,sum3):
            x=h2.pop(0)
            sum2=sum2-x
        elif sum3==max(sum1,sum2,sum3):
            x=h3.pop(0)
            sum3=sum3-x
    return sum1

if __name__ == '__main__':

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

