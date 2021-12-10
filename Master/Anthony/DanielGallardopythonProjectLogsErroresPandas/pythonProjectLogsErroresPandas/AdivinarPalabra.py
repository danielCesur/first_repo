import logging as log


class Juego:
    def __init__(self, numeroMaximoIntentos):
        self.numeroMaximoIntentos = numeroMaximoIntentos

    def num(self):
        log.info(self.numeroMaximoIntentos)


class JuegoNumero(Juego):
    def __init__(self, numeroMaximoIntentos, longitudPalabra):
        super().__init__(numeroMaximoIntentos)
        self.numero = longitudPalabra
        self.intentoActual = 0
        self.aciertoLongitud = False
        self.intentosNumeroLetras = []

    def adivinarLongitudPalabra(self):
        correcto = False
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
                    while not correcto:
                        self.intentoActual = input('Introduce un número menor:\n')
                        try:
                            self.intentoActual = int(self.intentoActual)
                            correcto = True
                            return self.aciertoLongitud
                        except:
                            log.warning("Solo se admiten números")

                elif self.numero > self.intentoActual:
                    while not correcto:
                        self.intentoActual = input('Introduce un número mayor:\n')
                        try:
                            self.intentoActual = int(self.intentoActual)
                            correcto = True
                            return self.aciertoLongitud
                        except:
                            log.warning("Solo se admiten números")

    def intentosMaximosRestantes(self):
        log.info("Te quedan solo " + str(self.numeroMaximoIntentos) + " intentos")


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
        global letra
        correcta = False
        while not correcta:
            letra = input("\nIntroduzca una letra de la palabra\n")
            if letra.isalpha():
                if len(letra) == 1:
                    letra = str(letra).upper()
                    self.intentosLetras.append(letra)
                    correcta = True
                else:
                    log.warning("\nSolo se admite UNA letra\n")
            else:
                log.warning("\nPor favor introduce una cadena de texto\n")

        if letra in self.palabraLista:
            log.info("\nEnhorabuena acertaste una letra")
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
        global palabra
        correcta = False
        while not correcta:
            palabra = input("Introduzca la palabra ")
            if palabra.isalpha():
                palabra = str(palabra).upper()
                self.intentosPalabras.append(palabra)
                correcta = True
            else:
                log.warning("\nPor favor introduce una cadena de texto\n")
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
        log.info('Tus intentos de longitud de palabra fueron ' + str(self.intentosNumeroLetras))
        log.info('Tus intentos de letras fueron ' + str(self.intentosLetras))
        log.info('Tus intentos de palabras fueron ' + str(self.intentosPalabras))

    def resultados(self):
        if self.victoria:
            log.info('Felicidades adivinaste la palabra')
            log.info(self.palabraAdivinar)
            self.resumen()
        else:
            log.info("La palabra a adivinar era " + self.palabraAdivinar)
            self.resumen()


if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    seguir = False
    while not seguir:
        numeroMaximoIntentos = input("Introduce la cantidad de intentos que tendrá el jugador\n")
        try:
            if int(numeroMaximoIntentos) > 0:
                numeroMaximoIntentos = int(numeroMaximoIntentos)
                seguir = True
            else:
                log.warning("\nIntroduce un número mayor que 0\n")
        except:
            log.warning("Solo se admiten números")

    cadenaCorrecta = False
    while not cadenaCorrecta:
        palabraAdivinar = input('Introduce la palabra que tendrá que adivinarse:\n')
        if palabraAdivinar.isalpha():
            longitudPalabraAdivinar = len(palabraAdivinar)
            game = JuegoPalabra(numeroMaximoIntentos, palabraAdivinar, longitudPalabraAdivinar)
            cadenaCorrecta = True
        else:
            log.warning("Por favor introduce una cadena de texto")

    seguir = False
    while not seguir:
        longitudPalabra = input('Introduce el número de letras que crees que tiene la palabra\n')
        try:
            longitudPalabra = int(longitudPalabra)
            game.intentoActual = longitudPalabra
            seguir = True
        except:
            log.warning("Solo se admiten números")

    while not game.victoria:
        if game.adivinarLongitudPalabra():
            while not game.final:
                seguir = False
                while not seguir:
                    log.info("\n1. Adivinar una letra\n2. Adivinar la palabra completa")
                    opcion = input("\nIntroduce la opcion:\n")
                    try:
                        opcion = int(opcion)
                        seguir = True
                    except:
                        log.warning("Solo se admiten números entre las opciones disponibles")

                if opcion == 1:
                    game.adivinarLetra()
                elif opcion == 2:
                    game.adivinarPalabra()
                else:
                    log.info("Introduce una opcion valida")

        if game.numeroMaximoIntentos <= 0:
            log.info("Te quedaste sin intentos, la longitud era " + str(game.longitudPalabra))
            break

    game.resultados()
