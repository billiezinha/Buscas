class Objeto:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.razao = round(valor / peso, 2)


def busca_gulosa(objetos, capacidade_maxima):
    objetos.sort(key=lambda x: x.razao, reverse=True)

    mochila = []
    peso_atual = 0
    valor_total = 0

    for obj in objetos:
        if peso_atual + obj.peso <= capacidade_maxima:
            mochila.append(obj)
            peso_atual += obj.peso
            valor_total += obj.valor

        if peso_atual == capacidade_maxima:
            break

    return {"mochila": mochila, "peso_atual": peso_atual, "valor_total": valor_total}


# Exemplos de uso
objetos = [
    Objeto('Estojo', 3, 80),
    Objeto('Caderno', 8, 100),
    Objeto('Garrafinha', 4, 60),
    Objeto('Casaco', 7, 120),
    Objeto('Computador', 35, 200)
]

capacidade_maxima = 20

resultado = busca_gulosa(objetos, capacidade_maxima)
print("Capacidade máxima da mochila:", capacidade_maxima)
print("Objetos selecionados na mochila:", [obj.nome for obj in resultado["mochila"]])
print("Peso total na mochila:", resultado["peso_atual"])
print("Valor total na mochila:", resultado["valor_total"])
