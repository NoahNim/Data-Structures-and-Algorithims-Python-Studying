def pair_product(numbers, target_product):
    previous = {}

    for n in range(0, len(numbers)):
        quotient = target_product // numbers[n]
        if quotient in previous:
            return (previous[quotient], n)
        else:
            previous[numbers[n]] = n
