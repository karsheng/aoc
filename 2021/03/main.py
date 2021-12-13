
def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()
            

def preprocess(bs):
    return [int(i) for i in bs]


def get_most_common(parsed, col):
    count = {
        0: 0,
        1: 0
    }
    for r in parsed:
        count[r[col]] += 1
    
    return 0 if count[0] > count[1] else 1

def generate_binary_string(parsed):
    binary_string = ""
    for i in range(len(parsed[0])):
        binary_string += str(get_most_common(parsed, i))
    return binary_string


def convert_to_decimal(binary_string):
    return int(binary_string, 2)

def reverse_binary_string(binary_string):
    reversed_string =""
    for c in binary_string:
        reversed_string += str(1-int(c))
    return reversed_string

data = parseFile("./example.txt")
parsed = [preprocess(l) for l in data]
bs = generate_binary_string(parsed)
rs = reverse_binary_string(bs)

print('q1', convert_to_decimal(bs)* convert_to_decimal(rs))

def oxygen_generator_rating(parsed, i):
    if len(parsed) == 1:
        string_ints = [str(i) for i in parsed[0]]
        return "".join(string_ints)

    most_common = get_most_common(parsed, i)
    filtered_parsed = [r for r in parsed if r[i] == most_common]
    return oxygen_generator_rating(filtered_parsed, i+1)


def co2_scrubber_rating(parsed, i):
    if len(parsed) == 1:
        string_ints = [str(i) for i in parsed[0]]
        return "".join(string_ints)

    least_common = 1 - get_most_common(parsed, i)
    filtered_parsed = [r for r in parsed if r[i] == least_common]
    return co2_scrubber_rating(filtered_parsed, i+1)

ogr = oxygen_generator_rating(parsed, 0)
csr = co2_scrubber_rating(parsed, 0)

print("q2", convert_to_decimal(ogr) * convert_to_decimal(csr))
