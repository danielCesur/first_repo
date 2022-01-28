intentosTotalPalabras = []
intentos = []
intentosPalabras = []
intentosFrases = []
aciertos = []


def almacenarFrase(frase):
    fraseAdivinar = frase.upper()
    fraseAdivinarDividida = fraseAdivinar.split()

    for palabra in fraseAdivinarDividida:
        for letra in palabra:
            aciertos.append('#')
        aciertos.append(' ')

    return fraseAdivinar


def cantidadDePalabras(frase):
    frase = frase.split()
    totalPalabras = 0
    for palabra in frase:
        totalPalabras += 1

    return totalPalabras


def comprobarAciertos(letra, fraseAdivinar):
    letras = []
    for posicion, caracter in enumerate(fraseAdivinar):
        if (caracter == letra):
            letras.append(posicion)

    for x in letras:
        aciertos[x] = letra


def comprobarPalabras(x, fraseAdivinar):
    posicionInicial = fraseAdivinar.find(x)
    for letra in x:
        aciertos[posicionInicial] = letra
        posicionInicial += 1


def dibujarFrase():
    for x in aciertos:
        print(x, end='')


def imprimirResultados():
    print('Los intentos de cantidad de palabras fueron ' + str(intentosTotalPalabras))
    print('Tus intentos de letras fueron ' + str(intentos))
    print('Tus intentos de palabras fueron ' + str(intentosPalabras))
    print('Tus intentos de frases fueron ' + str(intentosFrases))


def imprimirFinal(final):
    if final:
        print('Felicidades adivinaste la frase')
        print(fraseAdivinar)
        imprimirResultados()
    else:
        print('Te has quedado sin intentos, la frase era ' + fraseAdivinar)
        imprimirResultados()


def intentosRestantes(numeroMaxIntentos):
    if numeroMaxIntentos != 0:
        print('Te quedan solo ' + str(numeroMaxIntentos) + ' intentos')
    else:
        print('la cantidad de palabras era de ' + str(cantPalabras))


def opcionAdivinarLetra(numeroMaxIntentos, fraseAdivinar):
    print('Introduzca una letra que crea que este en la frase')
    intento = str(input()).upper()
    intentos.append(intento)
    if intento in fraseAdivinar:
        print("Felicidades adivinaste una letra")
        comprobarAciertos(intento, fraseAdivinar)
        dibujarFrase()
    else:
        numeroMaxIntentos -= 1
        if numeroMaxIntentos != 0:
            print('Te quedan solo ' + str(numeroMaxIntentos) + ' intentos')
            dibujarFrase()
        else:
            numeroMaxIntentos = 0

    return numeroMaxIntentos


def opcionAdivinarPalabra(numeroMaxIntentos, fraseAdivinar):
    print('Introduzca una palabra que crea que esta en la frase')
    intento = str(input()).upper()
    intentosPalabras.append(intento)
    if intento in fraseAdivinar:
        print("Felicidades adivinaste una palabra")
        comprobarPalabras(intento, fraseAdivinar)
        dibujarFrase()
    else:
        numeroMaxIntentos -= 1
        if numeroMaxIntentos != 0:
            print('Te quedan solo ' + str(numeroMaxIntentos) + ' intentos')
            dibujarFrase()
        else:
            numeroMaxIntentos = 0

    return numeroMaxIntentos


def opcionAdivinarFrase(numeroMaxIntentos, fraseAdivinar):
    global final
    print('Introduzca la frase que crea que es')
    intento = str(input()).upper()
    intentosFrases.append(intento)
    if intento == fraseAdivinar:
        final = True
        numeroMaxIntentos = 0
    else:
        numeroMaxIntentos -= 1
        if numeroMaxIntentos != 0:
            print('Te quedan solo ' + str(numeroMaxIntentos) + ' intentos')
            dibujarFrase()
        else:
            numeroMaxIntentos = 0

    return numeroMaxIntentos, final


if __name__ == '__main__':
    final = False
    fraseAdivinar = input('Introduce la frase que tendrá que adivinarse: ')
    frase = almacenarFrase(fraseAdivinar)
    cantPalabras = cantidadDePalabras(frase)
    numeroMaxIntentos = int(input('Introduce el número de intentos: '))

    while numeroMaxIntentos > 0:
        intentoTotalPalabras = input('adivina cuantas palabras hay ')
        intentoTotalPalabras = int(intentoTotalPalabras)
        intentosTotalPalabras.append(intentoTotalPalabras)

        if intentoTotalPalabras == cantPalabras:
            print('Acertaste la cantidad de palabras')
            dibujarFrase()

            while numeroMaxIntentos > 0:
                print('\nEscriba 1 para adivinar una letra')
                print('Escriba 2 para adivinar la palabra')
                print('Escriba 3 para adivinar la frase')
                opcion = int(input())

                if opcion == 1:
                    numeroMaxIntentos = opcionAdivinarLetra(numeroMaxIntentos, frase)
                if opcion == 2:
                    numeroMaxIntentos = opcionAdivinarPalabra(numeroMaxIntentos, frase)
                if opcion == 3:
                    numeroMaxIntentos, final = opcionAdivinarFrase(numeroMaxIntentos, frase)

        else:
            numeroMaxIntentos -= 1
            intentosRestantes(numeroMaxIntentos)

    imprimirFinal(final)
