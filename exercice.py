#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number > 0:
        return number
    return -number


def use_prefixes() -> List[str]:
    prefixes, suffixe = "JKLMNOPQ", "ack"

    return [p + suffixe for p in prefixes]


def prime_integer_summation() -> int:
    up_to = 100
    sqrt = (up_to ** 0.5) + 1
    primes = [2]
    for i in range(3, up_to + 1, 2):
        for p in primes:
            if p > sqrt:
                continue
            if i % p == 0:
                break
        else:
            primes.append(i)

    return sum(primes)


def factorial(number: int) -> int:
    # return number * factorial(number - 1)

    total = 1
    for n in range(2, number):
        total *= n

    return total


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_group(group: List[int]) -> bool:
    if any(age == 25 for age in group):
        return True
    if 3 <= len(group) and len(group) < 10:
        return False
    if any(age < 18 for age in group):
        return False
    if any(age > 70 for age in group) and any(age == 50 for age in group):
        return False
    return True


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return [verify_group(group) for group in groups]


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72],
        [18, 24, 22, 50, 70],
        [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20],
        [70, 50, 26, 28],
        [75, 50, 18, 25],
        [13, 25, 80, 15],
        [20, 30, 40, 50, 60],
        [75, 50, 100, 28],
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == "__main__":
    main()
