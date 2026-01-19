# Toteuta testi, jossa Pythonin listaan lisätään ensin luvut 1,2,\dots,n yksi kerrallaan listan loppuun. Tämän jälkeen listasta poistetaan n kertaa ensimmäinen alkio.
# Toteuta testi niin, että n=10^5. Mittaa kaksi aikaa: kauanko kestää lisätä luvut listalle ja kauanko kestää poistaa ne listalta.
# Tässä tehtävässä saat pisteen automaattisesti, kun ilmoitat tulokset ja käyttämäsi koodin ja painat lähetysnappia.

import time

def test(n: int):
    #lisääminen
    list = []
    start_add = time.time()
    for i in range(n+1):
        list.append(i)
    end_add = time.time()

    #poistaminen

    start_remove = time.time()
    while list:
        list.pop(0)
    end_remove = time.time()

    print(f"Lisäämiseen aikaa kului {end_add - start_add} s. Poistamiseen aikaa kului {end_remove - start_remove} s.")

test(10**5)