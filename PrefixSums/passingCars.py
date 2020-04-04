#A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
#
#Array A contains only 0s and/or 1s:
#
#0 represents a car traveling east,
#1 represents a car traveling west.
#The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
#
#For example, consider array A such that:
#
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
#
#The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
#
#For example, given:
#
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#the function should return 5, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer that can have one of the following values: 0, 1.

def solution(A):
    # A=010101の場合、右をPopすると01010が残り、1を取得する
    # 1を取得した場合、stackに+1する
    # 次に右をPopすると0101が残り、0を取得する
    # 0を取得した場合、stackの値をcountに追加する
    # Aが空になるまでくり返す
    # return count

    if len(A) < 1 or len(A) > 100000:
        return -1

    count = 0
    stack = 0
    while len(A) != 0:
        value = A.pop(-1)
        if value == 0:
            count = count + stack
        elif value == 1:
            stack = stack + 1
        else:
            return -1
    
        if count > 1000000000:
            return -1
    
    return count
