def prime_factors(n: int) -> list:
    factors = []
    i = 2
    # Обрабатываем двойку отдельно
    while n % i == 0:
        factors.append(i)
        n //= i

    i = 3
    # Идем по нечетным числам до корня из n
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # Если остаток больше 2, то это простое число
    if n > 2:
        factors.append(n)

    return factors

# Пример
n = 56
print(prime_factors(n))  # [2, 2, 2, 7]