

def first_decroissant(numbers):

    last, *numbers = numbers
    returned = []
    for number in numbers:
        if last > number:
            returned.append(number)
        last = number
    if len(returned) == 1:
        return returned[0]
    elif len(returned) == 0:
        raise ValueError("Given numbers don't follow the expected logic: not "
                         "contains decreasing number")
    else:
        assert len(returned) > 1
        raise ValueError("More than 1 decreasing number")



def run(payload):
    return first_decroissant((int(n) for n in payload.split()))
