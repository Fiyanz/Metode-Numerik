"""
Metode Tururnan Analitik
    - Metode Maju
    - Metode Mundur
    - Metode Tengah
"""

from fungsi import f, fh

def maju(x: int, h: float) -> float:
    """
    Fungsi Tururnan Metode Maju
    """
    return (fh(x + h) - (fh(x))) / h

def mundur(x: int, h: float) -> float:
    """
    Fungsi Tururnan Metode Mundur
    """
    return (fh(x) - fh(x - h)) / h

def tengah(x: int, h: float) -> float:
    """
    Fugnsi Tururnan Metode Tengah
    """
    return (fh(x + h) - fh(x - h)) / (2*h)

def newtonRapshon() -> float:
    """
    Fungsi Non Linier Terbuka
    """
# if __name__ == "__main__":
#     x, h = 2, 0.001
#     print(f"Hasil Motode Maju: {maju(x, h)}")
#     print(f"Hasil Metode Mundur: {mundur(x, h)}")
#     print(f"Hasil Metode Tengah: {tengah(x, h)}")
