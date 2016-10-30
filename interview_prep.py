
def matching_parentheses(str):
    c = 0
    for char in str:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
    return c == 0


if __name__ == '__main__':
    inp = input("#>")
    print(matching_parentheses(inp))