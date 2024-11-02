import metode


if __name__ == "__main__":

    h = 0.001
    
    for x in range(1, 30):
        hasilTengah = metode.tengah(x, h)
        print(f"Metode Tengengah index: {x}, Hasil: {hasilTengah}")
