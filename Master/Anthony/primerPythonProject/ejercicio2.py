class Juego:
    def __init__(self, numero, cantIntentos):
        self.numero = numero
        self.intento = 0
        self.victoria = False
        self.cantIntentos = cantIntentos
        self.intentos = []

    def adivinarNumero(self):
        self.intentos.append(self.intento)
        if self.numero == self.intento:
            self.victoria = True
            return self.victoria
        else:
            self.cantIntentos -= 1
            if self.cantIntentos <=0:
                return self.victoria
            else:
                self.intentosMaximosRestantes()
                if self.numero < self.intento:
                    self.intento = input('Introduce un número menor: ')
                    self.intento = int(self.intento)
                    return self.victoria
                elif self.numero > self.intento:
                    self.intento = input('Introduce un número mayor: ')
                    self.intento = int(self.intento)
                    return self.victoria

    def intentosMaximosRestantes(self):
        print("Te quedan solo " + str(self.cantIntentos) + " intentos")

    def resultados(self):
        print(self.intentos)


if __name__ == '__main__':
    numeroAdivinar = input('Introduce el número que ha de ser adivinado ')
    numeroAdivinar = int(numeroAdivinar)
    game = Juego(numeroAdivinar, 10)
    numIntento = input('Introduce un número para adivinar ')
    game.intento = int(numIntento)

    while not game.victoria:
        if game.adivinarNumero():
            print("Enhorabuena acertaste el número")
            break
        if game.cantIntentos <= 0:
            print("Te quedaste sin aciertos, el número era " + str(game.numero))
            break

    game.resultados()
