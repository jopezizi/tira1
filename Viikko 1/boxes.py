""" Sinun tulee pakata tuotteita laatikoihin. Jokaiseen laatikkoon mahtuu tietty määrä tuotteita. Montako laatikkoa tarvitset vähintään?
Esimerkiksi jos tuotteita on 10 ja yhteen laatikkoon mahtuu 3 tuotetta, tarvitset vähintään 4 laatikkoa. Voit esimerkiksi pakata laatikoihin 3, 3, 2 ja 2 tuotetta.
Toteuta tiedostoon boxes.py funktio min_count, joka antaa pienimmän laatikoiden määrän. Funktion parametrit ovat:

product_count: tuotteiden määrä
box_size: montako tuotetta laatikkoon mahtuu

Funktiosi toimintaa testataan suurella määrällä erilaisia testejä. Jokaisessa testissä molemmat parametrit ovat kokonaislukuja välillä 1–100.
 """

def min_count(product_count, box_size):
    full_boxes = product_count // box_size
    
    if product_count % box_size == 0:
        return full_boxes
    else:
        return full_boxes + 1
    
if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1