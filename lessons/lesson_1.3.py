# O(1)
print(1 + 1)

dadosA = list(range(10))
dadosB = list(range(10))

# O(n)
for i in dadosA:
    print(i)

print("------------------------")

# Propriedade da adição - O(n) + O(n) = O(2n) = O(n)
for i in dadosA:
    print(i)
for i in dadosB:
    print(i)

print("------------------------")

# Propriedade da multiplicação - O(n) * O(n) = O(n²)
for i in dadosA:
    for j in dadosB:
        print(i, j)

print("------------------------")

# Progressão aritmética - PA O(n²)
for i in dadosA:
    for j in dadosB:
        print(i, j)

print("------------------------")

dadosA = [0,1,2,3,4]

# Progressão geométrica - PG O(2ⁿ)
for i in dadosA:
    dadosB = list(range(0, (i*i), 1))
    for j in dadosB:
        print(f"i:{i} - j:{j}")