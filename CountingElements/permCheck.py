#A non-empty array A consisting of N integers is given.
#
#A permutation is a sequence containing each element from 1 to N once, and only once.
#
#For example, array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#    A[3] = 2
#is a permutation, but array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#is not a permutation, because value 2 is missing.
#
#The goal is to check whether array A is a permutation.
#
#Write a function:
#
#def solution(A)
#
#that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
#
#For example, given array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#    A[3] = 2
#the function should return 1.
#
#Given array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#the function should return 0.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    # write your code in Python 3.6
    # A.sort()でAの並び順を昇順にする
    # Aのindexに対する要素が(index+1)であることをチェックする
    # もし該当しないものを発見したら return 0
    # 全ての要素が条件を満たしたら return 1

    if len(A) < 1 or len(A) > 100000:
        return 0

    A.sort() # 昇順に変換
    for index in range(len(A)):
        if A[index] < 1 or A[index] > 1000000000:
            return 0
        if (index + 1) != A[index]:
            return 0

    return 1
