from peli import Peli


def main():
    while True:
        tulosta_ohjeet()
        pelimuoto = input("> ")[-1]
        if len(pelimuoto) == 0:
            print("Syötä pelimuoto")
            continue
        peli = None
        match pelimuoto:
            case 'a':
                peli = Peli.pelaaja_vs_pelaaja()
            case 'b':
                peli = Peli.pelaaja_vs_tekoaly()
            case 'c':
                peli = Peli.pelaaja_vs_parempi_tekoaly()
            case _:
               break
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
