import random
import sys
import math

def matching_parentheses(str):
    c = 0
    for char in str:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
    return c == 0

# better than linear time using modified binary search
# def find_missing_no(lst, left=0, right=(len(lst)-1), length=len(lst)):
#     if right <= left+1:
#         return left+1
#     else:
#         mid = (left+right) // 2
#         if mid - left != lst[mid] - lst[left]:
#             return find_missing_no

def coin_flip_probability(num_flips, num_heads):
    # given n flips, k heads, probability is:
    # (n choose k) p^n (1-p)^(n-k)
    # below we assume a fair coin (i.e. p = 0.5)

    p = 0.5
    nCk = math.factorial(num_flips) / (math.factorial(num_heads) * \
            math.factorial(num_flips - num_heads))
    
    return nCk * pow(p, num_heads) * pow(p, num_flips - num_heads)
  


if __name__ == '__main__':
    #inp = input("#>")
    #print(matching_parentheses(inp))
    #num_list = [x for x in range(101)]
    #del num_list[random.randint(0,99)]
    #print(num_list)
    #print(find_missing_no(num_list))
    print(coin_flip_probability(400, 220) * 100)
    