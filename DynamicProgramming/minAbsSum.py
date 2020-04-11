#For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:
#
#val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
#
#(Assume that the sum of zero elements equals zero.)
#
#For a given array A, we are looking for such a sequence S that minimizes val(A,S).
#
#Write a function:
#
#def solution(A)
#
#that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.
#
#For example, given array:
#
#  A[0] =  1
#  A[1] =  5
#  A[2] =  2
#  A[3] = -2
#your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..20,000];
#each element of array A is an integer within the range [−100..100].

def solution(A):
    # Aが与えられていて、val(A,S)が最小となる配列S (-1 or 1)を求める
    # その最小値をreturnする
    #
    # Sを直接求めるわけではないため、全ての符号を無視して、配列Aを２つのstackに足していき、差分を最小限になるようにする
    # そのためにはAを大きい順に並べる
    
    if len(A) < 0 or len(A) > 20000:
        return 0
    
    abs_A = map(abs, A)
    sorted_A = sorted(abs_A, reverse=True)
    stack_A = 0
    stack_B = 0
    
    for element_A in sorted_A:
        
        if element_A > 100:
            return 0
            
        if stack_A >= stack_B:
            stack_B = stack_B + element_A
        else:
            stack_A = stack_A + element_A
        
    result = abs(stack_A - stack_B)
    return result
