#Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.
#
#You start to eat the chocolates. After eating a chocolate you leave only a wrapper.
#
#You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.
#
#More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).
#
#You stop eating when you encounter an empty wrapper.
#
#For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.
#
#The goal is to count the number of chocolates that you will eat, following the above rules.
#
#Write a function:
#
#def solution(N, M)
#
#that, given two positive integers N and M, returns the number of chocolates that you will eat.
#
#For example, given integers N = 10 and M = 4. the function should return 5, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N and M are integers within the range [1..1,000,000,000].

def solution(N, M):
    # 一番シンプルな考え方は、１つずつN個のチョコレートをとっていく（該当のアドレスの値を0にする）
    # 円状のため、最大でも要素の数分繰り返す (for文で実現)
    # 作成した配列の値が0の時に繰り返した回数 countを返す
    
    if M < 1 or M > 1000000000:
        return 0
    if N <= 1 or M > 1000000000:
        return 0
    
    match_list = [1] * N
    count = 0
    prebious_point = 0
    for index in range(N):
        current_point =  (prebious_point + M) % N
        if match_list[current_point] == 0:
            return count
        match_list[current_point] = 0 # 一度遷移したポイントを次回以降踏めないようにする
        count = count + 1
        prebious_point = current_point
        
    return count
