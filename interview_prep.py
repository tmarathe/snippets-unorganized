import random
import sys
import math
import scipy.stats

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
    pdf_sum = 0
    for i in range(num_heads, num_flips+1):
        nCk = math.factorial(num_flips) / (math.factorial(i) * \
                                           math.factorial(num_flips - i))
        pdf_sum += nCk * pow(p, i) * pow(p, num_flips - i)

    return pdf_sum

def coin_flip_normal_approx(num_flips, num_heads):
    p = 0.5
    mean = num_flips * p
    var = mean * (1 - p)

    dist = scipy.stats.norm(mean, var)
    sig = math.sqrt(var)

    lim = (num_heads - mean)/sig
    return dist.cdf(lim)

if __name__ == '__main__':
    #inp = input("#>")
    #print(matching_parentheses(inp))
    #num_list = [x for x in range(101)]
    #del num_list[random.randint(0,99)]
    #print(num_list)
    #print(find_missing_no(num_list))
    print(coin_flip_probability(400, 220) * 100)
    print(coin_flip_normal_approx(400, 220) * 100)
    