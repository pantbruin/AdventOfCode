f = open('input.txt')
inp = [int(i) for i in f.read().splitlines()]

def sol_pt1(li):

    count = 0

    for i in range(1, len(li)):
        if li[i] > li[i - 1]:
            count += 1

    return count


def sol_pt2(li):

    count = 0

    first_window_sum = li[0] + li[1] + li[2]
    second_window_sum = 0

    for i in range(3, len(li)):
        second_window_sum = first_window_sum - li[i - 3] + li[i]

        if second_window_sum > first_window_sum:
            count += 1

        first_window_sum = second_window_sum

    return count

test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
