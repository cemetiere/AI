from pyswip import Prolog
import re

functions = {}
def store(d, name):
    def _(f):
        d[name] = f
        return f

    return _


@store(functions, "which_type")
def which_type(op):
    res = list(prolog.query(f'which_type(W,{op}).'))
    print(op, "type is ", end="")
    for value in res:
        print(value['W'] + ", ", end="")
    print()


@store(functions, "predecessor")
def predecessor(op):
    res = list(prolog.query(f'predecessor(W, {op}).'))
    print(op, "has predecessors: ", end="")
    for value in res:
        print(value['W'] + ", ", end="")
    print()


@store(functions, "descendant")
def descendant(op):
    res = list(prolog.query(f'descendant(W, {op}).'))
    print(op, "has descendants: ")
    for value in res:
        print(value['W'] + ", ")
    print()


@store(functions, "relative")
def interchangeable(op2, op1):
    res = bool(list(prolog.query(f'relative({op1}, {op2}).')))
    if res:
        print('Yes')
    else:
        print('No')



prolog = Prolog()
patterns = {
    r'Which type does (.+) have\?': 'which_type',
    r'What predecessors does (.+) have\?': 'predecessor',
    r'What descendants does (.+) have\?': 'descendant',
    r'Is (.+) relative for (.+)\?': 'relative'
}

KNOWLEDGE_BASE_PATH = './program.pl'
prolog.consult(KNOWLEDGE_BASE_PATH)
print('Knowledge base loaded')


while True:
    query = input('> ')
    if query.lower() == 'exit':
        break

    for pattern in patterns:
        match = re.match(pattern, query, re.IGNORECASE)
        if match is None:
            continue

        functions[patterns[pattern]](*match.groups())
        break
    else:
        print("Wrong query")