#An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
#
#For example, consider array A such that
#
# A[0] = 3    A[1] = 4    A[2] =  3
# A[3] = 2    A[4] = 3    A[5] = -1
# A[6] = 3    A[7] = 3
#The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
#Write a function
#
#def solution(A)
#
#that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.
#
#For example, given array A such that
#
# A[0] = 3    A[1] = 4    A[2] =  3
# A[3] = 2    A[4] = 3    A[5] = -1
# A[6] = 3    A[7] = 3
#the function may return 0, 2, 4, 6 or 7, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

def solution(A):
    # 与えられた配列Aの値がいくつずつ存在するか解るために、辞書型に変換する
    # 辞書dict_Aの最も数の多いKeyを取得する
    # そのKeyに該当する配列AのIndexを取得する
    
    dict_A = {}
    if len(A) < 0 or len(A) > 100000:
        return -1
    
    for element_A in A:
        if element_A < -2147483648 or element_A > 2147483647:
            return -1
        if element_A in dict_A:
            dict_A[element_A] = dict_A[element_A] + 1
        else:
            dict_A[element_A] = 1
            
    max_key = max(dict_A, key=dict_A.get)
    
    if dict_A[max_key] <= (len(A)/2): # 半分以上存在しない場合
        return -1
    
    index_result = A.index(max_key)
    return index_result
