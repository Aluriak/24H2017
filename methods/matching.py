

def closerof(opener):
    return {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }[opener]



def iscorrect(seq:str) -> bool:
    stack = []
    openers = '([{<'
    closers = ')]{>'
    for c in seq:
        if c in openers:
            stack.append(c)
        if c in closers:
            if c != closerof(stack[-1]):
                return False
    return True


def fix_matchs(seq:str) -> iter:
    stack = []
    openers = '([{<'
    closers = ')]{>'
    for c in seq:
        if c in openers:
            stack.append(c)
            yield c
        if c in closers:
            if c != closerof(stack[-1]):
                while c != closerof(stack[-1]):
                    stack.pop()
                yield c
    return
