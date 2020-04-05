#A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
#
#S is empty;
#S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
#S has the form "VW" where V and W are properly nested strings.
#For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
#Write a function:
#
#def solution(S)
#
#that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#
#For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..200,000];
#string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

def solution(S):
    # 文字列を配列に変換する => list_S
    # 左から１つずつPopしていく、stackに格納する
    # それぞれの条件式で、
    # "{", "[", "(" はstackにPushする
    # "}"はstackの先頭が"{"なら、"{"をPopする。違うなら return 0
    # "]"はstackの先頭が"["なら、"["をPopする。違うなら return 0
    # ")"はstackの先頭が"("なら、"("をPopする。違うなら return 0
    # list_Sが空 かつ stackが空なら return 1

    if len(S) < 0 or len(S) > 200000:
        return 0

    list_S = list(S)
    stack = []
    for element_S in list_S:
        if element_S == "{" or element_S == "[" or element_S == "(":
            stack.append(element_S)
        elif element_S == "}":
            if len(stack) > 0 and stack[len(stack)-1] == "{":
                stack.pop(-1)
            else:
                return 0
        elif element_S == "]":
            if len(stack) > 0 and stack[len(stack)-1] == "[":
                stack.pop(-1)
            else:
                return 0
        elif element_S == ")":
            if len(stack) > 0 and stack[len(stack)-1] == "(":
                stack.pop(-1)
            else:
                return 0
        else: # 該当しない文字の場合
            return 0
    
    if len(stack) == 0:
        return 1
