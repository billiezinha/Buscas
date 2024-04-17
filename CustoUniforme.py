# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({"cidade": vizinho, "custo": distancia})

# Função de busca de custo uniforme
def busca_de_custo_uniforme(origem, objetivo):
    borda = [{"cidade": origem, "caminho": [origem], "custo": 0}]
    visitados = set()

    while borda:
        borda.sort(key=lambda x: x["custo"])  # Ordena a borda com base no custo acumulado

        cidade_atual = borda.pop(0)  # Escolher o nó com menor custo e remover da borda
        cidade = cidade_atual["cidade"]
        caminho = cidade_atual["caminho"]
        custo = cidade_atual["custo"]

        if cidade == objetivo:
            return {"caminho": [c.nome for c in caminho], "custo": custo}

        visitados.add(cidade)

        for vizinho_info in cidade.vizinhos:
            vizinho = vizinho_info["cidade"]
            distancia = vizinho_info["custo"]
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]  # Caminho acumulado até o momento
                novo_custo = custo + distancia  # Custo acumulado até o momento
                borda.append({"cidade": vizinho, "caminho": novo_caminho, "custo": novo_custo})

    return None

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
arad.adicionar_vizinho(sibiu, 140)
arad.adicionar_vizinho(timisoara, 118)
arad.adicionar_vizinho(zerind, 75)

zerind.adicionar_vizinho(arad, 75)
zerind.adicionar_vizinho(oradea, 71)

oradea.adicionar_vizinho(zerind, 71)
oradea.adicionar_vizinho(sibiu, 151)

sibiu.adicionar_vizinho(arad, 140)
sibiu.adicionar_vizinho(fagaras, 99)
sibiu.adicionar_vizinho(oradea, 151)
sibiu.adicionar_vizinho(rimnicuVilcea, 80)

timisoara.adicionar_vizinho(arad, 118)
timisoara.adicionar_vizinho(lugoj, 111)

lugoj.adicionar_vizinho(timisoara, 111)
lugoj.adicionar_vizinho(mehadia, 70)

mehadia.adicionar_vizinho(lugoj, 70)
mehadia.adicionar_vizinho(dobreta, 75)

dobreta.adicionar_vizinho(mehadia, 75)
dobreta.adicionar_vizinho(craiova, 120)

craiova.adicionar_vizinho(dobreta, 120)
craiova.adicionar_vizinho(pitesti, 138)
craiova.adicionar_vizinho(rimnicuVilcea, 146)

rimnicuVilcea.adicionar_vizinho(sibiu, 80)
rimnicuVilcea.adicionar_vizinho(pitesti, 97)
rimnicuVilcea.adicionar_vizinho(craiova, 146)

fagaras.adicionar_vizinho(sibiu, 99)
fagaras.adicionar_vizinho(bucharest, 211)

pitesti.adicionar_vizinho(rimnicuVilcea, 97)
pitesti.adicionar_vizinho(craiova, 138)
pitesti.adicionar_vizinho(bucharest, 101)

bucharest.adicionar_vizinho(fagaras, 211)
bucharest.adicionar_vizinho(pitesti, 101)
bucharest.adicionar_vizinho(giurgiu, 90)
bucharest.adicionar_vizinho(urziceni, 85)

giurgiu.adicionar_vizinho(bucharest, 90)

urziceni.adicionar_vizinho(bucharest, 85)
urziceni.adicionar_vizinho(hirsova, 98)
urziceni.adicionar_vizinho(vaslui, 142)

hirsova.adicionar_vizinho(urziceni, 98)
hirsova.adicionar_vizinho(eforie, 86)

eforie.adicionar_vizinho(hirsova, 86)

vaslui.adicionar_vizinho(urziceni, 142)
vaslui.adicionar_vizinho(iasi, 92)

iasi.adicionar_vizinho(vaslui, 92)
iasi.adicionar_vizinho(neamt, 87)

neamt.adicionar_vizinho(iasi, 87)

# Execução da busca de custo uniforme
resultado = busca_de_custo_uniforme(sibiu, bucharest)

if resultado:
    print("Menor caminho:", resultado["caminho"])
    print("Custo total:", resultado["custo"])
else:
    print("Não foi possível encontrar um caminho.")
