#Write a function
#
#def solution(A)
#
#that, given an array A consisting of N integers, returns the number of distinct values in array A.
#
#For example, given array A consisting of six elements such that:
#
# A[0] = 2    A[1] = 1    A[2] = 1
# A[3] = 2    A[4] = 3    A[5] = 1
#the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    # dict_A = {:} を作成する
    # A = [2,1,1,2,3,1] の場合、dict_A = {1:3, 2:2, 3:1}となる辞書を作成する

    if len(A) <= 0 or len(A) > 100000:
        return 0

    dict_A = {}
    for element_A in A:
        if element_A in dict_A.keys():
            dict_A[element_A] = dict_A[element_A] + 1
        else:
            dict_A[element_A] = 1
    
        if abs(element_A) > 1000000:
            return 0

    return len(dict_A)
