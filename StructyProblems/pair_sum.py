def pair_sum(numbers, target_sum):
    previous = {}
    for n in range(0, len(numbers)):
        print(previous)
        difference = target_sum - numbers[n]
        if difference in previous:
            return (previous[difference], n)
        else:
            previous[numbers[n]] = n
