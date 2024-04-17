# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.distanciaObjetivo = distanciaObjetivo
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({"cidade": vizinho, "custo": distancia})

# Função de busca A*
def busca_a_estrela(inicio, objetivo):
    abertos = [inicio]  # Nós ainda não avaliados
    fechados = []  # Nós já avaliados
    caminho = {}

    # Função de custo total estimado
    def custo_total_estimado(cidade):
        return cidade.distanciaObjetivo + caminho[cidade.nome]["custo"]

    caminho[inicio.nome] = {"custo": 0, "pai": None}  # O custo para chegar à cidade inicial é 0 e não tem pai

    while abertos:
        # Encontrando a cidade com o menor custo total estimado
        cidade_atual = min(abertos, key=lambda cidade: custo_total_estimado(cidade))

        if cidade_atual == objetivo:
            caminho_final = []
            while cidade_atual:
                caminho_final.insert(0, cidade_atual.nome)
                cidade_atual = caminho[cidade_atual.nome]["pai"]
            return caminho_final

        # Removendo a cidade atual da lista de nós abertos
        abertos.remove(cidade_atual)
        fechados.append(cidade_atual)

        for vizinho in cidade_atual.vizinhos:
            if vizinho["cidade"] not in fechados:  # Se o vizinho ainda não foi avaliado
                custo_atualizado = caminho[cidade_atual.nome]["custo"] + vizinho["custo"]

                # Se o vizinho ainda não está na lista de nós abertos, ou se o novo custo é menor
                if vizinho["cidade"] not in abertos or custo_atualizado < caminho[vizinho["cidade"].nome]["custo"]:
                    caminho[vizinho["cidade"].nome] = {"custo": custo_atualizado, "pai": cidade_atual}  # Atualiza o custo e o pai do vizinho
                    if vizinho["cidade"] not in abertos:
                        abertos.append(vizinho["cidade"])  # Adiciona o vizinho à lista de nós abertos
    return None

# Criação do grafo
arad = Cidade("Arad", 366)
zerind = Cidade("Zerind", 374)
oradea = Cidade("Oradea", 380)
sibiu = Cidade("Sibiu", 253)
timisoara = Cidade("Timisoara", 329)
lugoj = Cidade("Lugoj", 244)
mehadia = Cidade("Mehadia", 241)
dobreta = Cidade("Dobreta", 242)
craiova = Cidade("Craiova", 160)
rimnicuVilcea = Cidade("Rimnicu Vilcea", 193)
fagaras = Cidade("Fagaras", 178)
pitesti = Cidade("Pitesti", 98)
bucharest = Cidade("Bucharest", 0)
giurgiu = Cidade("Giurgiu", 77)
urziceni = Cidade("Urziceni", 80)
hirsova = Cidade("Hirsova", 151)
eforie = Cidade("Eforie", 161)
vaslui = Cidade("Vaslui", 199)
iasi = Cidade("Iasi", 226)
neamt = Cidade("Neamt", 234)

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

# Execução da busca A*
resultado = busca_a_estrela(arad, bucharest)

if resultado:
    print("Caminho encontrado:")
    print(resultado)
else:
    print("Caminho não encontrado.")
