x = 10

def tes_scope():
    x = 20  # ini variabel lokal baru di dalam fungsi
    print("di dalam fungsi:", x)

tes_scope()
print("di luar fungsi:", x)