class Pessoa:
    olhos = 2
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
    thiago.olhos = 1
    del thiago.olhos
    print(thiago.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(thiago.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(renzo.olhos), id(thiago.olhos))
