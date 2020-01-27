class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    thiago = Pessoa(renzo, nome='Thiago')


    print(Pessoa.cumprimentar(thiago))
    print(id(thiago))
    print(thiago.cumprimentar())
    print(thiago.nome)
    print(thiago.idade)
    for filho in thiago.filhos:
        print(filho.nome)
    thiago.sobrenome='Ferreira'
    del thiago.filhos
    print(thiago.__dict__)
    print(renzo.__dict__)