def Main():
    s = 'GATATATGCATATACTT'
    t = 'ATAT'
    print(*[n + 1 for n in range(len(s)) if s.find(t, n) == n])

if __name__ == '__main__':
    Main()