def is_prime(n):
    if n == 1:
        return False
    for num in range(1, n):
        if n % num == 0 and num != 1 and num != n:
            return False
    return True
