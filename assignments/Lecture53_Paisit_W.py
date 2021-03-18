def vatCalculator(totalPrize):
    sum = totalPrize+(totalPrize*7/100)
    return sum

n = int(input())
print(vatCalculator(n))