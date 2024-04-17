# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho):
        self.vizinhos.append({"cidade": vizinho})


# Função de busca em profundidade limitada
def busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade):
    pilha = []
    visitados = set()

    pilha.append({"no": inicio, "profundidade": 0})
    visitados.add(inicio)

    while pilha:
        no_atual = pilha.pop()

        print(f"Visitando a cidade: {no_atual['no'].nome}")

        if no_atual["no"].nome == objetivo.nome:
            print(f"Encontrou o objetivo: {no_atual['no'].nome}")
            return True

        if no_atual["profundidade"] >= limite_profundidade:
            continue

        for vizinho_info in reversed(no_atual["no"].vizinhos):
            vizinho = vizinho_info["cidade"]
            if vizinho not in visitados:
                pilha.append({"no": vizinho, "profundidade": no_atual["profundidade"] + 1})
                visitados.add(vizinho)

    return False


# Função de busca em profundidade iterativa
def busca_profundidade_iterativa(inicio, objetivo):
    limite_profundidade = 0  # Inicializa o limite de profundidade

    while True:
        print(f"Tentando com limite de profundidade: {limite_profundidade}")

        encontrado = busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade)

        if encontrado:
            print(f"Objetivo encontrado com limite de profundidade {limite_profundidade}")
            return True
        else:
            print(f"Objetivo não encontrado com limite de profundidade {limite_profundidade}")
            limite_profundidade += 1


# Criação do grafo
arad = Cidade("Arad")
zerind = Cidade("Zerind")
oradea = Cidade("Oradea")
sibiu = Cidade("Sibiu")
timisoara = Cidade("Timisoara")
lugoj = Cidade("Lugoj")
mehadia = Cidade("Mehadia")
dobreta = Cidade("Dobreta")
craiova = Cidade("Craiova")
rimnicuVilcea = Cidade("Rimnicu Vilcea")
fagaras = Cidade("Fagaras")
pitesti = Cidade("Pitesti")
bucharest = Cidade("Bucharest")
giurgiu = Cidade("Giurgiu")
urziceni = Cidade("Urziceni")
hirsova = Cidade("Hirsova")
eforie = Cidade("Eforie")
vaslui = Cidade("Vaslui")
iasi = Cidade("Iasi")
neamt = Cidade("Neamt")

# Adicionando os vizinhos
arad.adicionar_vizinho(sibiu)
arad.adicionar_vizinho(timisoara)
arad.adicionar_vizinho(zerind)

zerind.adicionar_vizinho(arad)
zerind.adicionar_vizinho(oradea)

oradea.adicionar_vizinho(zerind)
oradea.adicionar_vizinho(sibiu)

sibiu.adicionar_vizinho(arad)
sibiu.adicionar_vizinho(fagaras)
sibiu.adicionar_vizinho(oradea)
sibiu.adicionar_vizinho(rimnicuVilcea)

timisoara.adicionar_vizinho(arad)
timisoara.adicionar_vizinho(lugoj)

lugoj.adicionar_vizinho(timisoara)
lugoj.adicionar_vizinho(mehadia)

mehadia.adicionar_vizinho(lugoj)
mehadia.adicionar_vizinho(dobreta)

dobreta.adicionar_vizinho(mehadia)
dobreta.adicionar_vizinho(craiova)

craiova.adicionar_vizinho(dobreta)
craiova.adicionar_vizinho(pitesti)
craiova.adicionar_vizinho(rimnicuVilcea)

rimnicuVilcea.adicionar_vizinho(sibiu)
rimnicuVilcea.adicionar_vizinho(pitesti)
rimnicuVilcea.adicionar_vizinho(craiova)

fagaras.adicionar_vizinho(sibiu)
fagaras.adicionar_vizinho(bucharest)

pitesti.adicionar_vizinho(rimnicuVilcea)
pitesti.adicionar_vizinho(craiova)
pitesti.adicionar_vizinho(bucharest)

bucharest.adicionar_vizinho(fagaras)
bucharest.adicionar_vizinho(pitesti)
bucharest.adicionar_vizinho(giurgiu)
bucharest.adicionar_vizinho(urziceni)

giurgiu.adicionar_vizinho(bucharest)

urziceni.adicionar_vizinho(bucharest)
urziceni.adicionar_vizinho(hirsova)
urziceni.adicionar_vizinho(vaslui)

hirsova.adicionar_vizinho(urziceni)
hirsova.adicionar_vizinho(eforie)

eforie.adicionar_vizinho(hirsova)

vaslui.adicionar_vizinho(urziceni)
vaslui.adicionar_vizinho(iasi)

iasi.adicionar_vizinho(vaslui)
iasi.adicionar_vizinho(neamt)

neamt.adicionar_vizinho(iasi)

# Execução da busca em profundidade iterativa
resultado = busca_profundidade_iterativa(arad, bucharest)

if resultado:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
