# DIAN KAMILAH
# 3337240077

# Matriks 1 (5x5)
matriks_1 = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9]
]

# Matriks 2 (5x5)
matriks_2 = [
    [9, 8, 7, 6, 5],
    [5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [0, 1, 0, 1, 0]
]

# Matriks hasil (5x5)
hasil = []

for i in range(5):  
    baris = []
    for j in range(5):  
        total = 0
        for k in range(5):
            total += matriks_1[i][k] * matriks_2[k][j]
        baris.append(total)
    hasil.append(baris)

# Tampilan hasil
print("Hasil Perkalian Matriks 5x5:")
for row in hasil:
    print(row)
