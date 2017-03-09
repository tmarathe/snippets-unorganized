import re

# implementation of a (very) basic four-function calculator
# takes well formed input expressions as strings
# for example: '1+1', '2 / 4 - 3', etc.

# this implementation uses regular expressions for parsing as opposed to recursive descent


def add_sub_expression(tokens):
    result, tokens = mult_div_term(tokens)
    while tokens[0] in ['+', '-']:
        if tokens[0] == '+':
            tokens = tokens[1:]
            result += mult_div_term(tokens)[0]
        if tokens[0] == '-':
            tokens = tokens[1:]
            result -= mult_div_term(tokens)[0]
    return result


def mult_div_term(tokens):
    result, tokens = atom(tokens)
    while tokens[0] in ['*', '/']:
        if tokens[0] == '*':
            tokens = tokens[1:]
            result *= mult_div_term(tokens)[0]
        elif tokens[0] == '/':
            tokens = tokens[1:]
            result /= mult_div_term(tokens)[0]

    return result, tokens


def atom(tokens):
    result = None
    if tokens[0].isdigit():
        result = float(tokens[0])
        tokens = tokens[1:]
    elif tokens[0] == '(':
        tokens = tokens[1:]
        result = add_sub_expression(tokens)
        tokens = tokens[1:]
    return result, tokens


if __name__ == '__main__':

    inp = input('Please enter a valid expression:')
    tokens = re.findall(r'[\d.]+|[\+\-*/()]', inp.replace(" ", ""))
    print(add_sub_expression(tokens))

