from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalt = False

    @abstractmethod
    def szobatipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def szobatipus(self):
        return "Egyágyas"

class KetagyasSzoba(Szoba):
    def szobatipus(self):
        return "Kétágyas"

class Foglalás:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szoba.foglalt:
                    print("Ez a szoba már foglalt.")
                    return
                else:
                    szoba.foglalt = True
                    foglalas = Foglalás(szoba, datum)
                    self.foglalasok.append(foglalas)
                    print("Sikeres foglalás.")
                    return
        print("Nem található ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                foglalas.szoba.foglalt = False
                self.foglalasok.remove(foglalas)
                print("Sikeres lemondás.")
                return
        print("Nem található ilyen foglalás.")

    def foglalasok_listazasa(self):
        print("Foglalások:")
        for foglalas in self.foglalasok:
            print(f"{foglalas.szoba.szobatipus()} szoba, szobaszám: {foglalas.szoba.szobaszam}, dátum: {foglalas.datum}")

def fill_data(szalloda):
    szalloda.uj_szoba(EgyagyasSzoba("101", 5000))
    szalloda.uj_szoba(EgyagyasSzoba("102", 5000))
    szalloda.uj_szoba(KetagyasSzoba("201", 8000))
    szalloda.uj_szoba(KetagyasSzoba("202", 8000))
    szalloda.uj_szoba(KetagyasSzoba("203", 8000))

    szalloda.foglalas("101", "2024-05-10")
    szalloda.foglalas("201", "2024-05-16")
    szalloda.foglalas("202", "2024-05-19")
    szalloda.foglalas("203", "2024-05-21")
    szalloda.foglalas("102", "2024-05-27")

def main():
    szalloda = Szalloda("Pici Pocok Szálloda")
    fill_data(szalloda)

    while True:
        print("\nVálassz műveletet:")
        print("1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Foglalások listázása")
        print("4 - Kilépés")

        valasztas = input("Művelet kiválasztása: ")

        if valasztas == "1":
            szobaszam = input("Add meg a szoba számát: ")
            datum = input("Add meg a foglalás dátumát (év-hó-nap formátumban): ")
            szalloda.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = input("Add meg a szoba számát: ")
            datum = input("Add meg a lemondás dátumát (év-hó-nap formátumban): ")
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.foglalasok_listazasa()
        elif valasztas == "4":
            break
        else:
            print("Hibás választás.")

if __name__ == "__main__":
    main()
