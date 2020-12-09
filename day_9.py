from itertools import combinations


if __name__ == "__main__":
    with open("day_9.input") as xmas_file:
        numbers = [int(line) for line in xmas_file]
    preamble_length = 25
    for i, n in enumerate(numbers[preamble_length:], start=preamble_length):
        preamble = numbers[i - preamble_length : i]
        valid_pairs = [p[0] + p[1] for p in combinations(preamble, 2)]
        if n not in valid_pairs:
            invalid_number = n
            print(n)
            break
    else:
        raise
    for i, n in enumerate(numbers):
        s = n
        smallest = largest = n
        while s < invalid_number:
            i += 1
            if numbers[i] < smallest:
                smallest = numbers[i]
            if numbers[i] > largest:
                largest = numbers[i]
            s += numbers[i]
        if s == invalid_number:
            print("%d + %d = %d" % (smallest, largest, smallest + largest))
            break
