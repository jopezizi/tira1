""" Helsingin yliopiston opiskelijanumero on numerosarja, jossa on yhdeksän numeroa. Ensimmäinen numero on 0 ja viimeinen numero on tarkastusnumero, jonka avulla voidaan havaita näppäilyvirhe opiskelijanumerossa.
Tarkastusnumero saadaan laskemalla summa muista numeroista kertoimilla 3,7,1,3,7,1,3,7 vasemmalta oikealle. Jos summa on tasakymmen, tarkastusnumero on 0. Muuten tarkastusnumero on etäisyys seuraavaan tasakymmeneen.
Esimerkiksi opiskelijanumerossa 012749139 summaksi tulee 3 \cdot 0 + 7 \cdot 1 + 1 \cdot 2 + 3 \cdot 7 + 7 \cdot 4 + 1 \cdot 9 + 3 \cdot 1 + 7 \cdot 3 = 91. Seuraava tasakymmen on 100, johon etäisyys on 9. Tämän takia opiskelijanumeron viimeinen numero on 9.
Toteuta tiedostoon student.py funktio check_number, joka ilmoittaa, onko parametrina annettu numerosarja oikein muodostettu opiskelijanumero. Funktion tulee palauttaa True tai False.
Funktiosi toimintaa testataan suurella määrällä erilaisia numerosarjoja. """

def check_number(number):
    
    if number[0] != '0' or len(number) != 9:
        return False
    
    check_input = number[:-1]
    sum = 0
    for i in range(len(check_input)):
        if i in [0,3,6]:
            sum += 3*int(check_input[i])
        elif i in [1,4,7]:
            sum += 7*int(check_input[i])
        elif i in [2,5]:
            sum += int(check_input[i])

    next = sum + (10 - sum % 10)

    if sum % 10 != 0:
        dist = next - sum
    else:
        dist = 0

    if number[-1] != str(dist):
        return False
    return True



if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False