import operator
from common import get_input

def solve(raw_input):
    gamma = epsilon = ""
    for j in range (len(raw_input[0])):
        count = {'0': 0, '1':0}
        for val in raw_input:
            count[val[j]] += 1
        if count['0'] > count['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(epsilon, 2) * int(gamma, 2)

def remove_bits(key, available, j, input):
    to_remove = set()
    for i in available:
        if input[i][j] != key:
            to_remove.add(i)
    return available-to_remove

def calculate_ratings(valid, input, op):
    comparators = {
        '>' : operator.gt,
        '<=': operator.le
    }
    for j in range (len(input[0])):
        if len(valid) == 1:
            break
        count = {'0': 0, '1':0}
        for i in valid:
            count[input[i][j]] += 1
        bit = '0' if comparators[op](count['0'], count['1']) else '1'
        valid = remove_bits(bit, valid, j, input)
    return valid.pop()

def solve_again(raw_input):
    valid = set([i for i in range(len(raw_input))])
    oxygen = calculate_ratings(valid, raw_input, '>')
    co2 = calculate_ratings(valid, raw_input, '<=')
    
    # return oxygen, co2
    return int(raw_input[oxygen], 2) * int(raw_input[co2], 2)

if __name__ == "__main__":
    raw = get_input("input/day_three.txt")
    print(solve_again(raw))