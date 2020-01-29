"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
    1) Atributo de dado velocidade
    2) Método acelerar, que deverá incremetar a velocidade de uma unidade
    3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
    1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
    2) Método girar_a_direita
    3) Método girar_a_esquerda

   N
O     L
   S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 0:
            if self.velocidade >= 2:
                self.velocidade -= 2
            else:
                self.velocidade -= 1


class Direcao:
    index: int = 0

    def __init__(self):
        #first mistake - self.valor = self.destinos()[]index(self.index).
        #Explanation: Variables cannot be accessed outside the scope of a function they were defined in.
        self.valor = self.destinos()[self.index]

    def posicao(self, sentido: int):
        self.index = self.index + sentido
        return self.index

    @staticmethod
    def destinos():
        #second error = list['Norte', 'Leste', 'Sul', 'Oeste']
        return ['Norte', 'Leste', 'Sul', 'Oeste']

    def girar_a_direita(self):
        if self.index == 3:
            # reseting
            self.index = 0
            self.valor = self.destinos()[self.posicao(0)]
        else:
            self.valor = self.destinos()[self.posicao(1)]

    def girar_a_esquerda(self):
        if self.index == 0:
            # reseting
            self.index = 3
            self.valor = self.destinos()[self.posicao(0)]
        else:
            self.valor = self.destinos()[self.posicao(-1)]


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

