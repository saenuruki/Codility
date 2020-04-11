#You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:
#
#with your first step you can stand on rung 1 or 2,
#if you are on rung K, you can move to rungs K + 1 or K + 2,
#finally you have to stand on rung N.
#Your task is to count the number of different ways of climbing to the top of the ladder.
#
#For example, given N = 4, you have five different ways of climbing, ascending by:
#
#1, 1, 1 and 1 rung,
#1, 1 and 2 rungs,
#1, 2 and 1 rung,
#2, 1 and 1 rungs, and
#2 and 2 rungs.
#Given N = 5, you have eight different ways of climbing, ascending by:
#
#1, 1, 1, 1 and 1 rung,
#1, 1, 1 and 2 rungs,
#1, 1, 2 and 1 rung,
#1, 2, 1 and 1 rung,
#1, 2 and 2 rungs,
#2, 1, 1 and 1 rungs,
#2, 1 and 2 rungs, and
#2, 2 and 1 rung.
#The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.
#
#Write a function:
#
#def solution(A, B)
#
#that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].
#
#For example, given L = 5 and:
#
#    A[0] = 4   B[0] = 3
#    A[1] = 4   B[1] = 2
#    A[2] = 5   B[2] = 4
#    A[3] = 5   B[3] = 3
#    A[4] = 1   B[4] = 1
#the function should return the sequence [5, 1, 8, 0, 1], as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#L is an integer within the range [1..50,000];
#each element of array A is an integer within the range [1..L];
#each element of array B is an integer within the range [1..30].

def getFibValue(value, fib_list):
    
    if not (value in fib_list.keys()):
        fib_list[value] = getFibValue((value-1), fib_list) + getFibValue((value-2), fib_list)
    return fib_list[value]

def solution(A, B):
    # L(1) = 1
    # L(2) = 2
    # L(3) = 3
    # L(4) = 5
    # L(5) = 8
    # Ladderの渡りかたはフィボナッチ数列的に増加していく
    #今回求める対象について
    # A=4,B=3 L(4) = 5 -> 5mod2^3 = 5
    # A=4,B=2 L(4) = 5 -> 5mod2^2 = 1
    # A=5,B=4 L(5) = 8 -> 5mod2^4 = 8
    # A=5,B=3 L(5) = 8 -> 5mod2^3 = 0
    # A=1,B=1 L(1) = 1 -> 5mod2^1 = 1
    
    if len(A) != len(B):
        return 0
    if len(A) < 1 or len(A) > 50000:
        return 0
    
    fib_list = {1:1, 2:2}
    result_list = []
    
    for index in range(len(A)):
        if A[index] < 1 or A[index] > len(A):
            return 0
        if B[index] < 1 or B[index] > 30:
            return 0
            
        fib_A = getFibValue(A[index], fib_list)
        result_list.append(fib_A % (2**B[index]))
    
    return result_list
