from decimal import getcontext, Decimal


def denominator_to_fraction(denominator):
    a = (Decimal(1.0) / Decimal(denominator), denominator)
    return a


def trim_both_ends_of_decimal_string(fraction_string):
    return fraction_string[12:-2]


def empty_string(string):
    return string


def determine_reciprocal_cycle(decimal_string):
    shortest_cycle = decimal_string
    full_len = len(decimal_string)
    half_len = full_len // 2
    second_half = half_len + 1
    at_least_one_match = False
    for i in range(full_len - 1, second_half, -1):
        cut_string = decimal_string[second_half: i]
        # print(cut_string)
        found = decimal_string.find(cut_string)

        if found:
            at_least_one_match == True

        test_string = cut_string + cut_string
        matches = decimal_string[found: found + len(test_string)] == test_string
        # print(test_string)
        # print(matches)

        if matches:
            shortest_cycle = cut_string
        else:
            if at_least_one_match:
                break
            else:
                pass

    return None if decimal_string == shortest_cycle else shortest_cycle


def main():
    # Set the precision.
    getcontext().prec = 10_000

    denominators = list(range(1, 20))
    decimals = map(denominator_to_fraction, denominators)
    decimal_strings = filter(empty_string, map(trim_both_ends_of_decimal_string, map(str, decimals)))
    recurring_cycles = list(map(determine_reciprocal_cycle, decimal_strings))
    # remove elements that aren't recurring
    filtered_recurring_cycles = list(filter(lambda x: x != None, recurring_cycles))
    cycles_lengths = list(map(len, filtered_recurring_cycles))
    max_length = max(cycles_lengths)
    pos_max_length = cycles_lengths.index(max_length)
    pos_decimal = recurring_cycles.index(filtered_recurring_cycles[pos_max_length])

    # arrays start at 0
    print(pos_decimal + 1)


if __name__ == "__main__":
    main()
