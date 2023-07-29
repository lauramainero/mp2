n = int(input())

taxas = []

for _ in range(n):
    taxa = float(input())

    taxas.append(taxa)

print('%.2f' % max(taxas))