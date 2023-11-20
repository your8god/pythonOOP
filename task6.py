phi = (2, 4, 3, 5, 6, 0, 7, 8, 1)

res = list(phi)
ord = 1
while ord < 95:
    for i, item in enumerate(res, 0):
        res[i] = phi[item]
    ord += 1
    print(f'ord{ord} =', *map(lambda x: x + 1, res))
    #if res == list(phi):
    #    break

print(ord)