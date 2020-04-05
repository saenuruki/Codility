#You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.
#
#The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.
#
#Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:
#
#0 represents a fish flowing upstream,
#1 represents a fish flowing downstream.
#If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:
#
#If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
#If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
#We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.
#
#For example, consider arrays A and B such that:
#
#  A[0] = 4    B[0] = 0
#  A[1] = 3    B[1] = 1
#  A[2] = 2    B[2] = 0
#  A[3] = 1    B[3] = 0
#  A[4] = 5    B[4] = 0
#Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.
#
#Write a function:
#
#def solution(A, B)
#
#that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.
#
#For example, given the arrays shown above, the function should return 2, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [0..1,000,000,000];
#each element of array B is an integer that can have one of the following values: 0, 1;
#the elements of A are all distinct.


class Fish():
    size = 0
    direction = 0
    def __init__(self,size,direction):
        self.size = size
        self.direction = direction
    

def solution(A, B):
    # 生存した魚の数を求める
    # 配列を0晩から順番に見ていく
    # １つめの値をStackに追加する
    # ２つめの値を追加する際に、
    # もし、stack[-1] == 0 and element_B ==
    # 最終的にresult_Bは <-,<-,<-,->,->のようになるつまり[0,0,0,1,1]
    stack = []

    if len(A) != len(B):
        return 0
        
    if len(A) < 1 or len(A) > 100000:
        return 0
    
    while len(A) != 0: # AとBは長さが同じ
    
        element_A = A.pop(0)
        element_B = B.pop(0)
        
        if len(stack) == 0: # stackが空の場合は、単純に追加する
            stack.append(Fish(element_A, element_B))
        else:
            if stack[-1].direction == 0 and element_B == 0: # 衝突しない
                stack.append(Fish(element_A, element_B))
            elif stack[-1].direction == 0 and element_B == 1: # 外向きのため衝突しない
                stack.append(Fish(element_A, element_B))
            elif stack[-1].direction == 1 and element_B == 0: # 衝突する
                if stack[-1].size < element_A:
                    stack.pop() # defaultは最後の値
                    stack.append(Fish(element_A, element_B))
                    # 逆の条件の場合は何もしない
                elif stack[-1].size == element_A:
                    return 0 # 同じ値は存在しない
            elif stack[-1].direction == 1 and element_B == 1: # 衝突しない
                stack.append(Fish(element_A, element_B))

    return len(stack)
