import re

# implementation of a (very) basic four-function calculator
# takes well formed input expressions as strings
# for example: '1+1', '2 / 4 - 3', etc.

# this implementation uses regular expressions for parsing as opposed to recursive descent

token_map = {}
token_map['+'] = 'ADD'
token_map['-'] = 'SUB'
token_map['*'] = 'MUL'
token_map['/'] = 'DIV'



if __name__ == '__main__':
    inp = input('Please enter a valid expression:')

    add_sub_tokens = re.split('(\+|\-)', inp.replace(" ", ""))
