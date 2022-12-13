from peli import Peli


def main():
    while True:
        tulosta_ohjeet()
        pelimuoto = input("> ")[-1]
        peli = Peli(pelimuoto)
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
