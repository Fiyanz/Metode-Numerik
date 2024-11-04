
def f(x: int) -> float:
    """
    Fungsi:
        x^3 + 4x + 1
    """
    # return x*x*x + 4*x + 1
    return 2*x**2 - 8

def regula_flasi(func, a: int, b: int, toll: float, i: int) -> float:
    fa = func(a)
    fb = func(b)

    for n in range(i):
        c = (fb * a - fa * b) / (fb - fa)
        fc = func(c)

        if abs(b - a) < toll * abs(b - a):
            break

        if (fc * fb) > 0:
            b = c
            fb = fc

        elif (fa * fc) > 0:
            a = c
            fa = fc
        else:
            break

    return c


if __name__ == "__main__":
    root = regula_flasi(f, 1, 3, 5e-15, 100)
    print(f"root: {root:.15f}")
