#A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
#
#For example, in array A such that:
#
#  A[0] = 9  A[1] = 3  A[2] = 9
#  A[3] = 3  A[4] = 9  A[5] = 7
#  A[6] = 9
#the elements at indexes 0 and 2 have value 9,
#the elements at indexes 1 and 3 have value 3,
#the elements at indexes 4 and 6 have value 9,
#the element at index 5 has value 7 and is unpaired.
#Write a function:
#
#def solution(A)
#
#that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
#
#For example, given array A such that:
#
#  A[0] = 9  A[1] = 3  A[2] = 9
#  A[3] = 3  A[4] = 9  A[5] = 7
#  A[6] = 9
#the function should return 7, as explained in the example above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an odd integer within the range [1..1,000,000];
#each element of array A is an integer within the range [1..1,000,000,000];
#all but one of the values in A occur an even number of times.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # Aから先頭１つをPopしてstack_Aに格納する
    # Aの次の先頭１つをPopして、stack_Aに一致するか判定し、
    # 一致する場合はstack_A内の一致した値をPopする
    # 一致しない場合はstack_Aに格納する
    # Aが空になるまで繰り返して、最後にstack_Aに残った値を返す
    
    stack_A = []
    
    if len(A) <= 0 or len(A) >= 1000000:
        return 0
        
    for element_A in A:
        if element_A <= 0 or element_A >= 1000000000:
            return 0
        if len(stack_A) > 0:
            flag = 0
            for stack_element_A in stack_A:
                if stack_element_A == element_A:
                    stack_A.remove(stack_element_A)
                    flag = 1
            if flag == 0:
                stack_A.append(element_A)
        else:
            stack_A.append(element_A)
    
    return stack_A[0]
