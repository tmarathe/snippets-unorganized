import random
import sys

def matching_parentheses(str):
    c = 0
    for char in str:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
    return c == 0

# better than linear time using modified binary search
def find_missing_no(lst, left=0, right=(len(lst)-1), length=len(lst)):
    if right <= left+1:
        return left+1
    else:
        mid = (left+right) // 2
        if mid - left != lst[mid] - lst[left]:
            return find_missing_no


    

if __name__ == '__main__':
    #inp = input("#>")
    #print(matching_parentheses(inp))
    


    num_list = [x for x in range(101)]
    del num_list[random.randint(0,99)]
    print(num_list)
    print(find_missing_no(num_list))
    