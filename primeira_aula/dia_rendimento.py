taxa = 1

taxas = []

while taxa != 0:
    taxa = float(input())

    if taxa == 0:
        break

    taxas.append(taxa)

print('%.2f' % max(taxas))