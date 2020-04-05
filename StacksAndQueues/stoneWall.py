#You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
#
#The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
#
#Write a function:
#
#def solution(H)
#
#that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
#
#For example, given array H containing N = 9 integers:
#
#  H[0] = 8    H[1] = 8    H[2] = 5
#  H[3] = 7    H[4] = 9    H[5] = 8
#  H[6] = 7    H[7] = 4    H[8] = 8
#the function should return 7. The figure shows one possible arrangement of seven blocks.
#
#
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array H is an integer within the range [1..1,000,000,000].

def solution(H):
    # if H is geven [8,8,5,7,9,8,7,4,8]
    # stack = [] <-8
    # stack = [8] <-8  # 8,8で揃った時はcountしない
    # stack = [8] <-5
    # stack = [5] <-7
    # stack = [5,7] <-9
    # stack = [5,7,9] <-8
    # stack = [5,7] <-7 #7,7で揃った時なcountしない
    # stack = [5,7] <-4
    # stack = [4] <-8

    count = 0
    stack = []
    
    if len(H) < 1 or len(H) > 100000:
        return 0
    
    for element_H in H:
        if element_H < 1 or element_H > 1000000000:
            return 0
        if len(stack) == 0:
            stack.append(element_H)
            count = count + 1
        else:
            if stack[-1] < element_H:
                stack.append(element_H)
                count = count + 1
            elif stack[-1] > element_H:
                stack = [x for x in stack if x <= element_H]
                count = count + 1
            # stack[-1] == element_Hの時は何もしない
            
    return count
