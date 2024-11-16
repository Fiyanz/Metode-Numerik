"""
Metode Tururnan Analitik
    - Metode Maju
    - Metode Mundur
    - Metode Tengah
"""

from fungsi import f

def maju(x: int, h: float) -> float:
    """
    Fungsi Tururnan Metode Maju

    arg:
        x: nilai x
        h: error / galat
    out:
        x: float
    """
    return (f(x + h) - (f(x))) / h

def mundur(x: int, h: float) -> float:
    """
    Fungsi Tururnan Metode Mundur

        arg:
        x: nilai x
        h: error / galat
    out:
        x: float
    """
    return (f(x) - f(x - h)) / h

def tengah(x: int, h: float) -> float:
    """
    Fugnsi Tururnan Metode Tengah

        arg:
        x: nilai x
        h: error / galat
    out:
        x: float
    """
    return (f(x + h) - f(x - h)) / (2*h)

