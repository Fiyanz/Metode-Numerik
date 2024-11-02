def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:  # Cek nilai fungsi
            return x
        fpx = f_prime(x)
        if fpx == 0:  # Cek jika turunan nol untuk menghindari pembagian oleh nol
            print("Turunan nol, metode gagal.")
            return None
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:  # Cek perubahan pada x
            return x_new
        x = x_new
    print("Gagal konvergen setelah iterasi maksimal.")
    return None

# Fungsi dan turunannya
# f = lambda x: x**2 - 2
# f_prime = lambda x: 2*x

f = lambda x: x**3 + 5*x + 15
f_prime = lambda x: 3*x**2 + 5


# Menjalankan metode Newton-Raphson
akar = newton_raphson(f, f_prime, x0=1.0)
print("Akar yang ditemukan:", akar)
