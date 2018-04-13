from functools import lru_cache

fib_terms = set()


@lru_cache()
def fib(num1, num2, limit):
    fib_terms.add(num1)
    fib_terms.add(num2)

    total = num1 + num2
    if total > limit:
        return num2
    else:
        return fib(num2, total, limit)


fib(1, 2, 4000000)
answer = 0
for term in fib_terms:
    if term % 2 == 0:
        answer += term

print('The answer is: {}'.format(answer))