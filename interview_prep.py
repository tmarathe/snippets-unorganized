import random
import sys
import math
import scipy.stats


# returns first unique character from a string. O(n)
def first_unique(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    for c in s:
        if d[c] == 1:
            print(c)


# 'melts' a histogram, returns path and number of steps until fully melted
def melt_histogram(arr):
    arr = [0] + arr + [0]
    arr2 = arr[:]
    counter = 0
    while sum(arr2) != 0:
        arr = arr2[:]
        print(arr2)
        for i in range(1, len(arr) - 1):
            if arr[i] - 1 >= 0:
                arr2[i] = min(arr[i - 1], arr[i] - 1, arr[i + 1])
            else:
                arr2[i] = 0
        counter += 1
    print(arr2)
    print("Number of steps: {}".format(counter))

# reverses a string in place. O(1) space, O(n) time.
def reverse_in_place(s):
    s = list(s)
    for i, j in zip(range(len(s) // 2), range(len(s) - 1, -1, -1)):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    print(''.join(s))


def matching_parentheses(str):
    c = 0
    for char in str:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
    return c == 0

# better than linear time using modified binary search
def find_missing_no(lst, left, right):

    # base case, ex: [4, 6]
    if right <= left+1:
        return left+1
    else:
        mid = left + (right - left)//2
        if lst[mid] - lst[left] != mid - left:
            return find_missing_no(lst, left, mid)
        elif lst[right] - lst[mid] != right - mid:
            return find_missing_no(lst, mid+1, right)

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

    num_list = [x for x in range(101)]
    rand_ind = random.randint(0,99)
    print(num_list[rand_ind])
    del num_list[rand_ind]
    print(find_missing_no(num_list, 0, len(num_list)-1))

    #print(coin_flip_probability(400, 220) * 100)
    #print(coin_flip_normal_approx(400, 220) * 100)

    #reverse_in_place("Hello, World!")

    #first_unique("abpcsdadpbc")

    #ex1 = [5, 4, 3, 6, 0, 1]
    # ex2 = [3, 1, 4, 1, 5, 1, 6, 1]
    # melt_histogram(ex2)
