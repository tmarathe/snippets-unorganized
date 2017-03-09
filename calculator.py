import re

# implementation of a (very) basic four-function calculator
# takes well formed input expressions as strings
# for example: '1+1', '2 / 4 - 3', etc.

# this implementation uses regular expressions for parsing as opposed to recursive descent

tm = {}
tm['+'] = 'ADD'
tm['-'] = 'SUB'
tm['*'] = 'MUL'
tm['/'] = 'DIV'

def expression(tokens):
    pass

def mult_div_term(tokens):
    result, tokens = atom(tokens)

    if tokens[0] == '*':
        tokens = tokens[1:]
        result *= mult_div_term(tokens)
    elif tokens[0] == '/':
        tokens = tokens[1:]
        result /= mult_div_term(tokens)

    return result, tokens


def atom(tokens):
    result = None
    if tokens[0].isdigit():
        result = float(tokens[0])
    elif tokens[0] == '(':
        result = expression(tokens[1:])
    else:
        return result, tokens
    return result, tokens[1:]


if __name__ == '__main__':

    inp = input('Please enter a valid expression:')
    tokens = re.findall(r'[\d.]+|[\+\-*/()]', inp.replace(" ", ""))

