def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Hasil untuk n = 1:", jumlah_n(1))
print("Hasil untuk n = 5:", jumlah_n(5))
print("Hasil untuk n = 10:", jumlah_n(10))
print("Hasil untuk n = 100:", jumlah_n(100))