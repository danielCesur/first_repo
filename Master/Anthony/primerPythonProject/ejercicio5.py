import random


class Juego:
    def __init__(self, numeroMaximoIntentos):
        self.numeroMaximoIntentos = numeroMaximoIntentos

    def num(self):
        print(self.numeroMaximoIntentos)


class JuegoNumero(Juego):
    def __init__(self, numeroMaximoIntentos, cantidadPalabras):
        super().__init__(numeroMaximoIntentos)
        self.numero = cantidadPalabras
        self.intentoActual = 0
        self.aciertoCantidad = False
        self.intentosCantidadTotalPalabras = []

    def adivinarCantidadPalabras(self):
        self.intentosCantidadTotalPalabras.append(self.intentoActual)
        if self.numero == self.intentoActual:
            self.aciertoCantidad = True
            return self.aciertoCantidad
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos <= 0:
                return self.aciertoCantidad
            else:
                self.intentosMaximosRestantes()
                if self.numero < self.intentoActual:
                    self.intentoActual = input('Introduce un número menor: ')
                    self.intentoActual = int(self.intentoActual)
                    return self.aciertoCantidad
                elif self.numero > self.intentoActual:
                    self.intentoActual = input('Introduce un número mayor: ')
                    self.intentoActual = int(self.intentoActual)
                    return self.aciertoCantidad

    def intentosMaximosRestantes(self):
        print("Te quedan solo " + str(self.numeroMaximoIntentos) + " intentos")


class JuegoPalabra(JuegoNumero):
    def __init__(self, numeroMaximoIntentos, cantidadPalabras):
        super().__init__(numeroMaximoIntentos, cantidadPalabras)
        self.victoria = False


class JuegoFrase(JuegoPalabra):
    def __init__(self, numeroMaximoIntentos, fraseAdivinar, cantidadPalabras):
        super().__init__(numeroMaximoIntentos, cantidadPalabras)
        self.fraseAdivinar = fraseAdivinar.upper()
        self.frase = self.fraseAdivinar.split()
        self.intentosTotalPalabras = []
        self.intentosLetras = []
        self.intentosPalabras = []
        self.intentosFrases = []
        self.aciertos = []
        self.comodines = []
        self.comodinesUsados = []
        self.final = False

        for palabra in self.frase:
            for _ in palabra:
                self.aciertos.append("#")
            self.aciertos.append(" ")

    def comprobarAcierto(self, letra):
        letras = []
        for posicion, caracter in enumerate(self.fraseAdivinar):
            if caracter == letra:
                letras.append(posicion)

        for x in letras:
            self.aciertos[x] = letra

    def comprobarPalabras(self, x):
        posicionInicial = self.fraseAdivinar.find(x)
        for letra in x:
            self.aciertos[posicionInicial] = letra
            posicionInicial += 1

    def dibujarFrase(self):
        for x in self.aciertos:
            print(x, end=" ")

    def resumen(self):
        print('Tus intentos de cantidad de palabras fueron ' + str(self.intentosCantidadTotalPalabras))
        print('Tus intentos de letras fueron ' + str(self.intentosLetras))
        print('Tus intentos de palabras fueron ' + str(self.intentosPalabras))
        print('Tus intentos de frases fueron ' + str(self.intentosFrases))
        print('Tus comodines usados han sido ' + str(self.comodinesUsados))

    def resultados(self):
        if self.victoria:
            print('Felicidades adivinaste la frase')
            print(self.fraseAdivinar)
            self.resumen()
        else:
            print("La frase a adivinar era " + self.fraseAdivinar)
            self.resumen()

    def definirComodines(self):
        for x in self.fraseAdivinar:
            if x not in self.comodines:
                self.comodines.append(x)

    def usarComodin(self):
        correcto = False
        while not correcto:
            comodin = random.choice(self.comodines)
            if comodin not in self.aciertos:
                correcto = True
                self.comprobarAcierto(comodin)
                self.dibujarFrase()
                self.comodinesUsados.append(comodin)

    def adivinarLetra(self):
        letra = str(input("Introduzca una letra que crea que este en la frase ")).upper()
        self.intentosLetras.append(letra)
        if letra in self.fraseAdivinar:
            print("Enhorabuena acertaste una letra")
            self.comprobarAcierto(letra)
            self.dibujarFrase()
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos != 0:
                self.intentosMaximosRestantes()
                self.dibujarFrase()
            else:
                self.final = True

    def adivinarPalabra(self):
        palabra = str(input("Introduzca la palabra ")).upper()
        self.intentosPalabras.append(palabra)
        if palabra in self.fraseAdivinar.upper():
            print("Enhorabuena acertaste una palabra")
            self.comprobarPalabras(palabra)
            self.dibujarFrase()
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos != 0:
                self.intentosMaximosRestantes()
                self.dibujarFrase()
            else:
                self.final = True

    def adivinarFrase(self):
        intento = str(input("Introduzca la frase que crea que es la correcta ")).upper()
        self.intentosFrases.append(intento)
        if intento == self.fraseAdivinar.upper():
            self.final = True
            self.victoria = True
        else:
            self.numeroMaximoIntentos -= 1
            if self.numeroMaximoIntentos != 0:
                self.intentosMaximosRestantes()
                self.dibujarFrase()
            else:
                self.final = True


if __name__ == '__main__':
    numeroMaximoIntentos = int(input("Introduce la cantidad de intentos que tendrá el jugador "))
    fraseAdivinar = input('Introduce la frase que tendrá que adivinarse: ')
    frase = fraseAdivinar.split()
    totalPalabras = 0
    for _ in frase:
        totalPalabras += 1

    game = JuegoFrase(numeroMaximoIntentos, fraseAdivinar, totalPalabras)

    cantidadPalabras = input('Introduce el número de palabras que crees que tiene la frase ')
    cantidadPalabras = int(cantidadPalabras)
    game.intentoActual = cantidadPalabras

    while not game.victoria:
        if game.adivinarCantidadPalabras():
            while not game.final:
                print(
                    "\n1. Adivinar una letra\n2. Adivinar una palabra\n3. Adivinar la frase completa\n4. Usar comodin")
                opcion = int(input("Introduce la opcion: "))
                if opcion == 1:
                    game.adivinarLetra()
                elif opcion == 2:
                    game.adivinarPalabra()
                elif opcion == 3:
                    game.adivinarFrase()
                elif opcion == 4:
                    game.definirComodines()
                    game.usarComodin()
        if game.numeroMaximoIntentos <= 0:
            print("Te quedaste sin intentos, la cantidad de palabras era " + str(totalPalabras))
            break

    game.resultados()
