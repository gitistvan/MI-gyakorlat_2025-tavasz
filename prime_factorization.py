import math

def prime_factors(n: int):
    """Return the list of prime factors of n."""
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def main():
    try:
        num = int(input("Adj meg egy egész számot: "))
    except ValueError:
        print("Érvénytelen bemenet.")
        return
    if num <= 1:
        print("A számnak nagyobbnak kell lennie 1-nél.")
        return
    factors = prime_factors(num)
    if len(factors) == 1 and factors[0] == num:
        print(f"{num} prím szám.")
    else:
        factor_str = " * ".join(map(str, factors))
        print(f"{num} prímtényezős felbontása: {factor_str}")


if __name__ == "__main__":
    main()
