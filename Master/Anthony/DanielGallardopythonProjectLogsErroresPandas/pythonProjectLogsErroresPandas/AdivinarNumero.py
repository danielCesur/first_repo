import logging as log


class Juego:
    def __init__(self, numero, cantIntentos):
        self.numero = numero
        self.intento = 0
        self.victoria = False
        self.cantIntentos = cantIntentos
        self.intentos = []

    def adivinarNumero(self):
        correcto = False
        self.intentos.append(self.intento)
        if self.numero == self.intento:
            self.victoria = True
            return self.victoria
        else:
            self.cantIntentos -= 1
            if self.cantIntentos <= 0:
                return self.victoria
            else:
                self.intentosMaximosRestantes()
                if self.numero < self.intento:
                    while not correcto:
                        self.intento = input('Introduce un número menor:\n')
                        try:
                            self.intento = int(self.intento)
                            correcto = True
                            return self.victoria
                        except:
                            log.warning("Solo se admiten números")

                elif self.numero > self.intento:
                    while not correcto:
                        self.intento = input('Introduce un número mayor:\n')
                        try:
                            self.intento = int(self.intento)
                            correcto = True
                            return self.victoria
                        except:
                            log.warning("Solo se admiten números")

    def intentosMaximosRestantes(self):
        log.info("Te quedan solo " + str(self.cantIntentos) + " intentos")

    def resultados(self):
        log.info(self.intentos)


if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    valido = False
    while not valido:
        numeroAdivinar = input('Introduce el número que ha de ser adivinado\n')
        try:
            numeroAdivinar = int(numeroAdivinar)
            valido = True
        except:
            log.warning("Solo se admiten números")

    game = Juego(numeroAdivinar, 10)
    valido = False

    while not valido:
        numIntento = input('Introduce un número para adivinar\n')
        try:
            game.intento = int(numIntento)
            valido = True
        except:
            log.warning("Solo se admiten números")

    while not game.victoria:
        if game.adivinarNumero():
            log.info("Enhorabuena acertaste el número")
            break
        if game.cantIntentos <= 0:
            log.info("Te quedaste sin aciertos, el número era " + str(game.numero))
            break

    game.resultados()
