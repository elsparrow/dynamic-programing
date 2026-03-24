import math
import random

"""
function to find minimal checks to find out at what height a ball breaks
n = number of stories (in building), k = number of balls.
"""
def checking_number (n: int, k: int) ->int:

    arr = [0] * (k + 1) # Each index in arr represents the amount of floors able to check given the amount of balls in that index, that grows by the amount of tries (counter)
    counter = 0 # to count the number of moves.
    while arr[k] < n: # while the amount of floors able to check with k balls is smaller than n
        counter += 1
        for i in range(k, 0, -1): # iterate the checks for each ball
            arr[i] += 1 + arr[i - 1]
    return counter # return the number of moves found.

"""
function to find floor where balls will break.
given two bals (k = 2) and n floors
"""
def index_floor(f_i: list[int], b: int) -> int:
    ans = -1 # default output if ball doesnt break.
    n = len(f_i)
    step = index_first_floor(n) # step to jump to if 1st ball doesnt break. (using first floor to check method for efficiency)
    curr = step - 1
    prev  = 0 # to remember the last step checked.
    while curr < n: # make sure were in bounds.
        if b < f_i[curr]: # 1st ball breaks.
            ans = f_i[curr]
            for j in range(prev, curr): # linear search (from last place known the ball doesent break up to where it broke.
                if b < f_i[j]: # 2nd ball breaks.
                    ans = f_i[j] # breaking point found!
                    break
            break
        else:
            prev = curr + 1
            step -= 1
            curr += step
    return ans

"""
function to find the first floor needed to check for n floors and given two balls
"""
def index_first_floor (n: int) ->int:
    return math.ceil((math.sqrt(1 + 8*n) - 1)/2) # formula



if __name__ == '__main__':

    print("question 1: ")
    n0 = random.randint(1,1000)
    k0 = random.randint(1,1000)
    print("floors: {}".format(n0))
    print("balls: {}".format(k0))
    print(checking_number(100,2))
    """
    """
    print("question 2: ")
    f1 = sorted(random.sample(range(1, 100), 7))
    b1 = random.randint(1,100)
    print("f1: {}".format(f1))
    print("b1: {}".format(b1))
    ans1 = index_floor(f1, b1)
    print("ans1: {},".format(ans1))
    """
    """
    f2 = sorted(random.sample(range(1, 1000), 99))
    b2 = random.randint(1, 1000)
    print("f2: {}".format(f2))
    print("b2: {}".format(b2))
    ans2 = index_floor(f2, b2)
    print("ans2: {},".format(ans2))
    """
    """
    f3 =sorted(random.sample(range(1, 100), 2))
    b3 = random.randint(1, 100)
    print("f3: {}".format(f3))
    print("b3: {}".format(b3))
    ans3 = index_floor(f3, b3)
    print("ans3: {},".format(ans3))
    print("question 3: ")
    n1 = random.randint(1, 1000)
    print(n1)
    print(index_first_floor (n1))