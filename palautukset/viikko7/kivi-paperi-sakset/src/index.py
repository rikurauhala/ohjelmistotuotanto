from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


def main():
    while True:
        tulosta_ohjeet()
        vastaus = input("> ")
        valinta = vastaus[-1]
        peli = None
        match valinta:
            case 'a':
                peli = KPSPelaajaVsPelaaja()
            case 'b':
                peli = KPSTekoaly()
            case 'c':
                peli = KPSParempiTekoaly()
            case _:
                break
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli.pelaa()


def tulosta_ohjeet():
    ohjeet = [
        "Valitse pelataanko",
        "(a) Ihmistä vastaan",
        "(b) Tekoälyä vastaan",
        "(c) Parannettua tekoälyä vastaan",
        "Muilla valinnoilla lopetetaan"
    ]
    print("\n".join(ohjeet))


if __name__ == "__main__":
    main()
