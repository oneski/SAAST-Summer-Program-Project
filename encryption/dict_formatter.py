from string import ascii_lowercase

def line_formatter(li):
    #exclude = [",", ".", ";", ":", "'", " ", "!", "\xef", "\"]

    new_vals = []

    for line in li:
        new_lines = [l.lower() for l in line if l.isalpha()]
        new_vals.append(''.join(new_lines))

    return new_vals

def gen_dict(filename):
    lines = gen_list(filename)

    #print lines
    result = {chr(c) : 0 for c in range(ord('a'), ord('z') + 1)}

    for line in lines:
        # gen_sub_dict returns a dictionary with the counts of each letter of the string
        subdict = gen_sub_dict(line)
        for key in subdict.keys():
            result[key] += subdict[key]

    return result

def gen_list(filename):
        with open(filename) as f:
            return line_formatter([f.strip().replace(" ", "") for f in f.readlines() if f.strip() != ""])

def calc_frequency(dic):
    '''
    Takes in a dictionary where {(letter) : count(letter)}
    '''
    total = 0.0
    for key in dic.keys():
        total += dic[key]
    return {key : "{:.1f}".format(100 * (dic[key] / total)) for key in list(ascii_lowercase)}

def gen_sub_dict(s):
    counts = [s.count(chr(c)) for c in range(ord('a'), ord('z') + 1)]
    z = zip(list(ascii_lowercase), counts)
    content = {k : v for k, v in z}
    return content

def subCipher(ciphertext, outfile, filename = "subst-table-ex.txt"):
    subDict = tbl(filename)
    result = []
    out = open(outfile, 'w')

    for line in ciphertext:
        out.write("".join(subDict[char] for char in line))
        out.write("\n")

    out.close()
def tbl(filename):
    output = {}

    with open(filename) as f:
        lines = f.readlines()

    for i in range(26):
        output[chr(i + 97)] = lines[i].strip()
        
    return output

def to_file(list_, outfile):
    out = open(outfile, 'w')
    
    for line in list_:
        out.write("".join(line))
        out.write("\n")

    out.close()

'''
    the disarm codes are under their very noses 
    to be rather than to seem 
'''
