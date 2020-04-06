#A non-empty array A consisting of N integers is given.
#
#The leader of this array is the value that occurs in more than half of the elements of A.
#
#An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
#
#For example, given array A such that:
#
#    A[0] = 4
#    A[1] = 3
#    A[2] = 4
#    A[3] = 4
#    A[4] = 4
#    A[5] = 2
#we can find two equi leaders:
#
#0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
#2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
#The goal is to count the number of equi leaders.
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
#
#For example, given:
#
#    A[0] = 4
#    A[1] = 3
#    A[2] = 4
#    A[3] = 4
#    A[4] = 4
#    A[5] = 2
#the function should return 2, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

def solution(A):
    # 左右２つに分割して、同じリーダーを持つ組み合わせを返す
    # リーダーとは半数より多い値が最大値であること
    # 配列Aの最大値を求めて、Aの値を最大値である場合は1、それ以外の値は0に置き換える
    # for文で２分した両者のリーダーが等しい時にcount +1する
    # return count
    
    if max(A) > 1000000000 or min(A) < -1000000000:
        return 0
    if len(A) < 1 or len(A) > 100000:
        return 0
        
    max_value = max(A)
    checkList_A = list(map(lambda x: 1 if x == max_value else 0, A))
    count = 0
    for index_A in range(len(checkList_A)):
        left_list = checkList_A[0:index_A]
        right_list = checkList_A[index_A:len(checkList_A)]
        if len(left_list) > 0 and len(right_list) > 0:
            if sum(left_list)/len(left_list) > 0.5 and sum(right_list)/len(right_list) > 0.5:
                count = count + 1
    return count
