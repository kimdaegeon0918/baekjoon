# 보석 도둑
# Gold 5, 수학

n = int(input())

i = 2
factors = []
while i*i<=n:
    if n%i:
        i += 1
    else:
        n //= i
        factors.append(i)
if n>1:
    factors.append(n)

print(len(factors))
print(*factors)