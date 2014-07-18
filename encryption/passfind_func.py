def create_inventory(s):

    letter_list = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    counts = [s.count(chr(c)) for c in range(ord('a'), ord('z') + 1)]
    z = zip(letter_list, counts)
    return {k : v for k, v in z}

def subtract(li1, li2):
    
    result = {}
    diffs = []
    for i in range(0, len(li1.values())):
        diffs.append(abs(li1[chr( ord('a') + i )] - li2[chr( ord('a') + i)]))
    z = zip([chr(c) for c in range(ord('a'), ord('z') + 1)], diffs)
    return {k : v for k,v in z}

def is_in(li1, li2):
    v1 = li1.values()
    v2 = li2.values()
    bools = []

    for i in range(0, len((v1)) - 1):
        if (v1[i] > 0):
            bools.append(v2[i] > 0)
    return False not in bools


def to_str(li):
    values = li.values()
    keys = li.keys()

    result = ""

    for i in range(0, len(keys) - 1):
        result += values[i] * str(keys[i])
    return result

print subtract(create_inventory("hello"), create_inventory("helloworld"))