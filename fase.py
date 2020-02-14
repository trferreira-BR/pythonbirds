# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO


VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []


    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase

        :param obstaculos:
        """
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase

        :param porcos:
        """
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase

        :param passaros:
        """
        self._passaros.extend(passaros)

    def status(self):
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return:
        """
        countPorcosAtivos = 0
        countPassarosAtivos = 0

        for porco in self._porcos:
            if porco.status == ATIVO:
                countPorcosAtivos += 1
        for passaro in self._passaros:
            if passaro.status == ATIVO:
                countPassarosAtivos += 1

        if countPorcosAtivos > 0 and countPassarosAtivos > 0:
            return EM_ANDAMENTO

        if countPorcosAtivos > 0:
            return DERROTA

        if countPorcosAtivos == 0:
            return VITORIA

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """
        for passaro in self._passaros:
            if not passaro.foi_lancado():
                passaro.lancar(angulo, tempo)
                break


    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela de acordo ao tempo e ao estado dos atores.

        Cada ator deve ser transformado em um Ponto, mas antes, precisa ser levado em consideração o seguinte:
        -Antes dos atores serem transformados em ponto, os mesmos devem ter noção do tempo e intervalo de colisão
        com base na fase atual.
            *Calcule a posição do passáro de acordo com o tempo.
                -Implemente a função _calcula_posicao_passaro_pelo_tempo()
            *Realize a colisão dos passáros de acordo com os obstáculos e os porcos com base no intervalo de colisão
                -Implemente a função _causar_colisao_passaro()

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        for passaro in self._passaros:
            self._calcula_posicao_passaro_pelo_tempo(passaro, tempo)
            self._causar_colisao_passaro(passaro)

        pontos=[self._transformar_em_ponto(a) for a in self._passaros+self._obstaculos+self._porcos]

        return pontos

    def _causar_colisao_passaro(self, passaro):
        # for ponto in self._obstaculos + self._porcos:
        #     passaro.colidir(ponto, self.intervalo_de_colisao)
        # passaro.colidir_com_chao()
        pass

    def _calcula_posicao_passaro_pelo_tempo(self, passaro, tempo):
        # passaro.calcular_posicao(tempo)
        pass

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())

