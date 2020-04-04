#A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
#
#Count the minimal number of jumps that the small frog must perform to reach its target.
#
#Write a function:
#
#def solution(X, Y, D)
#
#that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
#
#For example, given:
#
#  X = 10
#  Y = 85
#  D = 30
#the function should return 3, because the frog will be positioned as follows:
#
#after the first jump, at position 10 + 30 = 40
#after the second jump, at position 10 + 30 + 30 = 70
#after the third jump, at position 10 + 30 + 30 + 30 = 100
#Write an efficient algorithm for the following assumptions:
#
#X, Y and D are integers within the range [1..1,000,000,000];
#X ≤ Y.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
  # write your code in Python 3.6
  # correct_distance = Y - X : YとXの相対距離を保持する
  # (correct_distance // D) + 1 を返す


  if X <= 0 or X > 1000000000:
    return 0
  if Y <= 0 or Y > 1000000000:
    return 0
  if D <= 0 or D > 1000000000:
    return 0
  if X >= Y:
    return 0
  
  correct_distance = Y - X

  if correct_distance < D:
    return 1
  result = (correct_distance // D)
  if correct_distance % D != 0:
    result = result + 1

  return result
