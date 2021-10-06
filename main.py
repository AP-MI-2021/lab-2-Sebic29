from math import sqrt
from datetime import date

'''
Găsește ultimul număr prim mai mic decât un număr dat.
'''


def is_prime(n):
    # Aceasta functie returneaza daca un numar este prim
    # parametrul n este numarul dat pentru care se returneaza daca este prim
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_largest_prime_below(n):
    # Aceasta functie returneaza cel mai mare numar prim mai mic decat un numarul introdus
    for i in range(n - 1, 2, -1):
        if is_prime(i):
            return i
    return 0


def test_get_largest_prime_below():
    # Testaza niste valori pentru functia get_largest_below
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(7) == 5


'''
Calculează CMMMC al n numere date.
'''


def cmmdc(x, y):
    # Calculeza cel mai mic divizor comun al numerelor x si y introduse  ca parametrii
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    return x


def cmmmmc(x, y):
    # Calculeaza si determina cel mai mare multiplu comun al numerelor x,y
    return (x * y) // cmmdc(x, y)


def get_cmmmc(list):
    # Determina cmmmc ul a n numere introduse intr o lista(lst)
    n = len(list)
    c = cmmmmc(list[0], list[1])
    for i in range(2, n):
        c = cmmmmc(c, list[i])
    return c


def test_get_cmmmc():
    assert get_cmmmc([4, 6, 8]) == 24
    assert get_cmmmc([5, 12, 4]) == 60
    assert get_cmmmc([3, 8, 9]) == 72


'''
Afișează toate pătratele perfecte dintr-un interval închis dat.
'''


def get_perfect_squares(start: int, end: int):
    # Returneaza patratele perfecte din intervalul dat prin paramentrii start si end
    list_of_perfect_numbers = []
    for number in range(start, end + 1):
        if sqrt(number) == int(sqrt(number)):
            list_of_perfect_numbers.append(int(number))

    return list_of_perfect_numbers


def test_get_perfect_squares():
    assert get_perfect_squares(10, 20) == [16]
    assert get_perfect_squares(20, 40) == [25, 36]
    assert get_perfect_squares(50, 100) == [64, 81, 100]


'''
Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime
'''


def is_superprime(n) :
    #Determina daca un numar este super prim
    while n:
        if is_prime(n) :
            n = n // 10
        else :
            return False
    return True


def test_is_superprime() :
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(239) == True
    assert is_superprime(404) == False


def main():
    while True:
        print("\nAlegeti o optiune din urmatoarele. ")
        print("1.Determina ultimul număr prim mai mic decât un număr dat. ")
        print("2.Calculeaza cmmmc a n numere date. ")
        print("3.Afiseaza patratele perfecte dintr un interval inchis. ")
        print("4.Determina daca un numar este superprim. ")
        print("5.Iesire din program\n")
        optiune = int(input("Alegeti o optiune din urmatoarele: "))
        if optiune == 1:
            x = int(input("Dati un numar prim: "))
            print(get_largest_prime_below(x))
        elif optiune == 2:
            numbers_str = input("Introduceti numerele: ")
            numbers_str = numbers_str.split(' ')
            list_of_numbers = []
            for number in numbers_str:
                list_of_numbers.append(int(number))

            rezult = get_cmmmc(list_of_numbers)
            print(f"Cmmmc ul numerelor introduse este: {rezult}")
        elif optiune == 3:
            capat_stanga_interval = int(input("Capat stanga de interval: "))
            capat_dreapta_interval = int(input("Capat dreaota de interval: "))
            final_list = []
            final_list = get_perfect_squares(capat_stanga_interval, capat_dreapta_interval)
            print(f"Patratele perfecte din intevral sunt: {final_list}")
        elif optiune == 4:
            numar = int(input("Introduceti numarul: "))
            rez = is_superprime(numar)
            print(f"Rezultat: {rez}")
        elif optiune == 5 :
            break

if __name__ == '__main__':
    main()

