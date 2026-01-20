""" Vuosi 2026 on erityinen vuosi, koska 2^2+0^2+2^2+6^2=44 eli vuosiluvun numeroiden neliöiden summassa jokainen numero on sama.
Toteuta tiedostoon special.py funktio check_year, joka ilmoittaa, onko parametrina annettu vuosi erityinen vuosi. Funktion tulee palauttaa True tai False.
Funktiosi toimintaa testataan suurella määrällä erilaisia testejä. Jokaisessa testissä vuosiluku on välillä 1000–9999. """

def check_year(year):
    year = list(str(year))
    sum = 0
    for num in year:
        sum += int(num) ** 2

    num_1 = str(sum)[0]
    for num in str(sum):
        if num != num_1:
            return False
    
    return True

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2000)) # True
    print(check_year(2026)) # True
    print(check_year(2029)) # False
    print(check_year(9215)) # True