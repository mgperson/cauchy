from itertools import permutations, product


def problem(n):
    l = range(1, n + 1)
    for p in permutations(l):
        for coefs in product([-1, 1], repeat=n):
            yield map(lambda t: t[0] * t[1], zip(coefs, p))


def format(results):
    results = list(results)
    print (len(results))
    for r in results:
        print (" ".join(map(str, r)))


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    #n = int(open(dirname(__file__) + '/data.txt').read())
    format(problem(3))