def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print('Compound Interest is', CI)

compound_interest(10000, 10.25, 5)