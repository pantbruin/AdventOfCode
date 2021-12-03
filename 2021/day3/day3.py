f = open('input.txt')
inp = [i for i in f.read().splitlines()]

def sol_1(i):

    storage = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0], 11: [0, 0], 12: [0, 0]}

    for bin_string in i:
        for i in range(len(bin_string)):
            if bin_string[i] == '0':
                storage[i + 1][0] += 1
            else:
                storage[i + 1][1] += 1

    gamma = []
    epsilon = []

    for i in range(1, 13):
        if storage[i][0] > storage[i][1]:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    gamma_string = "".join(gamma)
    epsilon_string = "".join(epsilon)

    gamma_int = int(gamma_string, 2)
    epsilon_int = int(epsilon_string, 2)

    return gamma_int * epsilon_int


def count_frequency(index, li, which_rating_string):
    frequencies = {'0': 0, '1':0}
    for element in li:
        frequencies[element[index]] += 1

    if which_rating_string == 'co2':
        return '0' if frequencies['0'] <= frequencies['1'] else '1'
    else:
        return '1' if frequencies['1'] >= frequencies['0'] else '0'

def extract_valid_numbers(li, filter_digit, index):

    return [number for number in li if number[index] == filter_digit]

def sol_2(i, rating):

    result = i

    ind = 0

    while len(result) != 1:
        most_common = count_frequency(ind, result, rating)
        result = extract_valid_numbers(result, most_common, ind)
        ind += 1

    return int(result[0], 2)


test = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

oxygen_rating = sol_2(inp, 'o2')
carbon_rating = sol_2(inp, 'co2')
print(oxygen_rating * carbon_rating)