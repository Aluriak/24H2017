

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
    closers = ')]}>'
    for c in seq:
        if c in openers:
            stack.append(c)
        if c in closers:
            if c != closerof(stack[-1]):
                return False
            stack.pop()
    return not stack


def close_all(seq:str) -> iter:
    stack = []
    openers = '([{<'
    closers = ')]}>'
    for idx, c in enumerate(seq):
        if c in openers:
            stack.append(c)
        if c in closers:
            if c != closerof(stack[-1]):
                raise ValueError("Unexpected unvalid input seq.")
            stack.pop()
    # return the missing ones
    return ''.join(closerof(opener) for opener in reversed(stack))


def run(payload:str) -> str:
    return close_all(payload)
