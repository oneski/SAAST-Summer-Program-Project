def formatter(dic):
    exclude = [",", ".", ";", ":", "'", " ", "!"]
    keys = dic.keys()
    vals = dic.values()

    new_vals = []

    for line in vals:
        new_lines = [l.lower() for l in line if l not in exclude]
        new_vals.append(''.join(new_lines))

    z = zip(keys, new_vals)

    return {k : v for k, v in z}

print formatter({"la" : "Hello.", "lad" : "Hello", "lads" : "me;sd.F!"})