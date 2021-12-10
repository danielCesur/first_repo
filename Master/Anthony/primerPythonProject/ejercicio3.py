class Juego:
    def __init__(self, numeroMaximoIntentos):
        self.numeroMaximoIntentos = numeroMaximoIntentos

    def num(self):
        print(self.numeroMaximoIntentos)


class JuegoNumero(Juego):
    def __init__(self, numeroMaximoIntentos, longitudPalabra):
        super().__init__(numeroMaximoIntentos)
        self.numero = longitudPalabra
        self.intentoActual = 0
        self.aciertoLongitud = False
        self.intentosNumeroLetras = []

    def adivinarLongitudPalabra(self):
        self.intentosNumeroLetras.append(self.intentoActual)
        if self.numero == self.intentoActual:
            self.aciertoLongitud = True
            return self.aciertoLongitud
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos <= 0:
                return self.aciertoLongitud
            else:
                self.intentosMaximosRestantes()
                if self.numero < self.intentoActual:
                    self.intentoActual = input('Introduce un número menor: ')
                    self.intentoActual = int(self.intentoActual)
                    return self.aciertoLongitud
                elif self.numero > self.intentoActual:
                    self.intentoActual = input('Introduce un número mayor: ')
                    self.intentoActual = int(self.intentoActual)
                    return self.aciertoLongitud

    def intentosMaximosRestantes(self):
        print("Te quedan solo " + str(self.numeroMaximoIntentos) + " intentos")


class JuegoPalabra(JuegoNumero):
    def __init__(self, numeroMaximoIntentos, palabraAdivinar, longitudPalabra):
        super().__init__(numeroMaximoIntentos, longitudPalabra)
        self.palabraAdivinar = palabraAdivinar
        self.longitudPalabra = longitudPalabra
        self.intentosPalabras = []
        self.intentosLetras = []
        self.aciertos = []
        self.palabraLista = list(self.palabraAdivinar.upper())
        self.victoria = False
        self.final = False

        for x in self.palabraAdivinar:
            self.aciertos.append('#')

    def comprobarAcierto(self, letra):
        letras = []
        for posicion, caracter in enumerate(self.palabraAdivinar.upper()):
            if caracter == letra:
                letras.append(posicion)

        for x in letras:
            self.aciertos[x] = letra

    def dibujarPalabra(self):
        for x in self.aciertos:
            print(x, end='')

    def adivinarLetra(self):
        letra = str(input("Introduzca una letra de la palabra ")).upper()
        self.intentosLetras.append(letra)
        if letra in self.palabraLista:
            print("Enhorabuena acertaste una letra")
            self.comprobarAcierto(letra)
            self.dibujarPalabra()
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos != 0:
                self.intentosMaximosRestantes()
                self.dibujarPalabra()
            else:
                self.final = True

    def adivinarPalabra(self):
        palabra = str(input("Introduzca la palabra ")).upper()
        self.intentosPalabras.append(palabra)
        if palabra == self.palabraAdivinar.upper():
            self.final = True
            self.victoria = True
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos != 0:
                self.intentosMaximosRestantes()
                self.dibujarPalabra()
            else:
                self.final = True

    def resumen(self):
        print('Tus intentos de longitud de palabra fueron ' + str(self.intentosNumeroLetras))
        print('Tus intentos de letras fueron ' + str(self.intentosLetras))
        print('Tus intentos de palabras fueron ' + str(self.intentosPalabras))

    def resultados(self):
        if self.victoria:
            print('Felicidades adivinaste la palabra')
            print(self.palabraAdivinar)
            self.resumen()
        else:
            print("La palabra a adivinar era " + self.palabraAdivinar)
            self.resumen()


if __name__ == '__main__':
    numeroMaximoIntentos = int(input("Introduce la cantidad de intentos que tendrá el jugador "))
    palabraAdivinar = input('Introduce la palabra que tendrá que adivinarse: ')
    longitudPalabraAdivinar = len(palabraAdivinar)
    game = JuegoPalabra(numeroMaximoIntentos, palabraAdivinar, longitudPalabraAdivinar)

    longitudPalabra = input('Introduce el número de letras que crees que tiene la palabra ')
    longitudPalabra = int(longitudPalabra)
    game.intentoActual = longitudPalabra

    while not game.victoria:
        if game.adivinarLongitudPalabra():
            while not game.final:
                print("\n1. Adivinar una letra\n2. Adivinar la palabra completa")
                opcion = int(input("Introduce la opcion: "))
                if opcion == 1:
                    game.adivinarLetra()
                elif opcion == 2:
                    game.adivinarPalabra()

        if game.numeroMaximoIntentos <= 0:
            print("Te quedaste sin intentos, la longitud era " + str(game.longitudPalabra))
            break

    game.resultados()
