#A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
#
#Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
#
#The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
#
#In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
#
#For example, consider array A such that:
#
#  A[0] = 3
#  A[1] = 1
#  A[2] = 2
#  A[3] = 4
#  A[4] = 3
#We can split this tape in four places:
#
#P = 1, difference = |3 − 10| = 7
#P = 2, difference = |4 − 9| = 5
#P = 3, difference = |6 − 7| = 1
#P = 4, difference = |10 − 3| = 7
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
#
#For example, given:
#
#  A[0] = 3
#  A[1] = 1
#  A[2] = 2
#  A[3] = 4
#  A[4] = 3
#the function should return 1, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [2..100,000];
#each element of array A is an integer within the range [−1,000..1,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 絶対値:abs(element)
    # pointerをずらしながら、全ての差分をresult_arrayに格納する
    # result_array.min()で最小値を取得して返す

    if len(A) == 1:
        return sum(A)
    if len(A) <= 0 or len(A) > 100000:
        return 0
    
    result_array = []
    for pointer in range(len(A)):
    
        if pointer >= 1 or pointer <= (len(A)-1):
            left_sum_A = sum(A[0:pointer])
            right_sum_A = sum(A[pointer:len(A)])
            result_array.append(abs(left_sum_A - right_sum_A))

    return min(result_array)
