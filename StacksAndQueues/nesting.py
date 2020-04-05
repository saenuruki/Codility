#A string S consisting of N characters is called properly nested if:
#
#S is empty;
#S has the form "(U)" where U is a properly nested string;
#S has the form "VW" where V and W are properly nested strings.
#For example, string "(()(())())" is properly nested but string "())" isn't.
#
#Write a function:
#
#def solution(S)
#
#that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
#
#For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..1,000,000];
#string S consists only of the characters "(" and/or ")".

def solution(S):
    # "("の場合は単純にstackに追加する
    # ")"の場合、stack.pop()が"("かどうかを判定する
    # もし正しい場合は次に進む (既にpopしているため)
    # もし誤りの場合は、return 0
    # 最後まで進み、len(stack)==0の場合 return 1
    # それ以外はreturn 0
    
    list_S = list(S)
    stack = []
    
    if len(list_S) < 0 or len(list_S) > 1000000:
        return 0
    
    for element_S in list_S:
        if element_S == "(":
            stack.append(element_S)
        elif element_S == ")":
            if len(stack) <= 0 or stack.pop() != "(":
                return 0
        else: # "(",")"以外は受け入れない
            return 0
    
    if len(stack) == 0:
        return 1
    else:
        return 0
