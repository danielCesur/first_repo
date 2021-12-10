class Juego:
    def __init__(self, numero):
        self.numero = numero
        self.intento = 0
        self.victoria = False

    def adivinarNumero(self):
        if self.numero < self.intento:
            self.intento = input('Introduce un número menor: ')
            self.intento = int(self.intento)
            return self.victoria
        elif self.numero > self.intento:
            self.intento = input('Introduce un número mayor: ')
            self.intento = int(self.intento)
            return self.victoria
        elif self.numero == self.intento:
            self.victoria = True
            return self.victoria


if __name__ == '__main__':
    numeroAdivinar = input('Introduce el número que ha de ser adivinado ')
    numeroAdivinar = int(numeroAdivinar)
    game = Juego(numeroAdivinar)
    numIntento = input('Introduce un número para adivinar ')
    game.intento = int(numIntento)

    while not game.victoria:
        if game.adivinarNumero():
            break

    print("Enhorabuena acertaste el número")
