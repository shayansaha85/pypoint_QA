def divide_count_of_list(l, n):
    count = 0
    for i in range(len(l)):
        if n % l[i] == 0:
            count += 1
    return count


def lcm(user_in):
    numbers = []

    for i in range(0, len(user_in.split())):
        numbers.append(int(user_in.split()[i]))

    numbers.sort()
    maxVal = numbers[-1]

    i = 1

    while i > 0:
        result = maxVal * i
        if divide_count_of_list(numbers, result) == len(numbers):
            print(f'LCM = {result}')
            break
        else:
            i = i + 1


n = input()
lcm(n)