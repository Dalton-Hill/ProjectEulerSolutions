from functools import reduce


def is_prime(num):
    """
    Returns a boolean value that will signify if the number given is prime or not.

    Args::

        n (int):  # the number to test

    Returns::

        bool:  # True if n is prime, False if not

    """
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


if __name__ == '__main__':
    goal = 600851475143
    factors = []
    for n in range(1, goal):
        if goal % n == 0 and is_prime(n):
            factors.append(n)
            if reduce(lambda x, y: x*y, factors) == goal:
                break
    print('Answer: {}'.format(max(factors)))