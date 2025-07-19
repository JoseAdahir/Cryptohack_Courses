state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def matrix2bytes(matrix):
    text = []
    for i in matrix:        
        text+= i
    return bytes(text)


def add_round_key(s, k):
    r = matrix2bytes(s)
    t = matrix2bytes(k)
    final = bytes([a^i for a,i in zip(r,t)])
    return final

print(add_round_key(state, round_key))

