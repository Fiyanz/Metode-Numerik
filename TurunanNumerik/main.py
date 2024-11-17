import metode
import fungsi

def f(x):
    # Fungsi yang ingin dioptimasi: f(x) = x^2 + 4x + 4
    # return x**2 + 4*x + 4
    return x**3 + 5*x + 15

def central_difference(x, h=0.001):
    # Metode Beda Pusat untuk aproksimasi turunan pertama
    return (f(x + h) - f(x - h)) / (2 * h)

def gradient_descent(initial_x, learning_rate=0.1, tolerance=1e-6, max_iterations=1000):
    x = initial_x
    for iteration in range(max_iterations):
        grad = central_difference(x)  # Hitung turunan menggunakan metode beda pusat
        new_x = x - learning_rate * grad  # Update nilai x
        
        # Cek konvergensi jika perubahan sangat kecil
        if abs(new_x - x) < tolerance:
            print(f"Converged after {iteration} iterations.")
            break
        
        x = new_x
    
    return x




if __name__ == "__main__":

    h = 0.001
    
    for x in range(30):
        hasilNumerik = metode.tengah(x, h)
        hasilAnalitik = fungsi.fh(x)
        print(f"Index: {x}, Hasil Analitik: {hasilAnalitik}, Hasil Numerik: {hasilNumerik}")


    # Inisialisasi parameter
    initial_x = 0  # Titik awal
    learning_rate = 0.1  # Laju pembelajaran
    tolerance = 1e-6  # Toleransi konvergensi

    # Jalankan Gradient Descent
    minimum_x = gradient_descent(initial_x, learning_rate, tolerance)
    minimum_value = f(minimum_x)

    print(f"Nilai minimum ditemukan pada x = {minimum_x}")
    print(f"Nilai minimum fungsi f(x) = {minimum_value}")