import metode
import fungsi

if __name__ == "__main__":

    h = 0.00000000000001
    
    for x in range(1, 30 + 1):
        hasilNumerik = metode.tengah(x, h)
        hasilAnalitik = fungsi.fh(x)
        print(f"Index: {x}, Hasil Analitik: {hasilAnalitik}, Hasil Numerik: {hasilNumerik}")
