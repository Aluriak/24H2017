



def run(payload):
    animals = tuple(payload.strip().splitlines())

    rev_animals = tuple(''.join(reversed(name)) for name in animals)
    sorted_rev = sorted(rev_animals)
    return '\n'.join(''.join(reversed(name))
                     for name in sorted_rev)


