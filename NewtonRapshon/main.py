def f(x: int) -> int:
    """
    fungsi utama x^3 + 5*x + 15
    """
    return x**3 + 5*x + 15

def fp(x: int) -> int:
    """
    fungsi dari x^3 + 5*x + 15

    f'(x) = 3x^2 + 5
    """

    return 3*x**2 + 5


def newtonRapshon(x0: int, toll: float, max_iterasi: int) -> float:
    """
    Fungsi Non Linier Terbuka
    """
    x = x0
    for i in range(max_iterasi):
        fx = f(x)

        if abs(fx) < toll:
            return x

        fxp = fp(x)
        if abs(fxp) == 0:
            print("Turunan Bernilai 0, Gagal")
            return None
        new_x = x - fx / fxp
        if abs(new_x) < toll:
            return new_x
        x = new_x

    print("Gagal Menemukan X")
    return None



if __name__ == "__main__":
    x0 = 3
    toll = 0.1
    max_iterasi = 30

    hasil = newtonRapshon(x0, toll, max_iterasi)
    print(hasil)
