#A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
#
#For example, array A such that:
#
#  A[0] = -3
#  A[1] = 1
#  A[2] = 2
#  A[3] = -2
#  A[4] = 5
#  A[5] = 6
#contains the following example triplets:
#
#(0, 1, 2), product is −3 * 1 * 2 = −6
#(1, 2, 4), product is 1 * 2 * 5 = 10
#(2, 4, 5), product is 2 * 5 * 6 = 60
#Your goal is to find the maximal product of any triplet.
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A, returns the value of the maximal product of any triplet.
#
#For example, given array A such that:
#
#  A[0] = -3
#  A[1] = 1
#  A[2] = 2
#  A[3] = -2
#  A[4] = 5
#  A[5] = 6
#the function should return 60, as the product of triplet (2, 4, 5) is maximal.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [3..100,000];
#each element of array A is an integer within the range [−1,000..1,000].

def solution(A):
    # 配列内の値のうち最大値３つの掛け合わせを返す問題と読み替える
    # A.sort() により、配列を昇順に並び替える
    # この場合、２つの回答の可能性がある。
    # max3 = 配列の昇順により、大きい値を３つ取得する
    # max1_min2 = 大きい値１つと小さい値２つを取得する (マイナス*マイナスはプラスのため)

    if len(A) < 3 or len(A) > 100000:
        return 0

    A.sort()
    if A[0] < -1000 or A[-1] > 1000:
        return 0
    
    max3 = A[-3] * A[-2] * A[-1]
    max1_min2 = A[-1] * A[0] * A[1]

    if max3 > max1_min2:
        return max3
    else:
        return max1_min2
