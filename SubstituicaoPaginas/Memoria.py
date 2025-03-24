import random
import hashlib
import sys

class MemoriaSecundaria:

    def __init__(self, qtPaginas):
        self.qtPaginas = qtPaginas
        self.__leituras = 0

        self.__memoria = []
        for i in range(self.qtPaginas):
            self.__memoria.append([])
            for j in range(4):
                self.__memoria[i].append(geraHash((i+1)*(j+1)))

    def getPagina(self, pagina):
        if pagina >= self.qtPaginas:
            print(f'MemoriaSecundaria: tentativa de acesso a pagina fora do limite. Limite({self.qtPaginas}) Pagina de Acesso ({pagina})' )
            sys.exit(0)
        self.__leituras = self.__leituras + 1
        return self.__memoria[pagina]
    
    def getLeituras(self):
        return self.__leituras

class MemoriaPrincipal:

    def __init__(self, qtPaginas):
        self.qtPaginas = qtPaginas
        self.__leituras = 0
        self.__escritas = 0

        self.__memoria = []
        for i in range(self.qtPaginas):
            self.__memoria.append([])
            for j in range(4):
                self.__memoria[i].append(0)

    def getPagina(self, endereco):
        if endereco >= self.qtPaginas:
            print(f'MemoriaPrincipal: tentativa de acesso a pagina fora do limite. Limite({self.qtPaginas}) Pagina de Acesso ({endereco})' )
            sys.exit(0)
        self.__leituras = self.__leituras + 1
        return self.__memoria[endereco]
    
    def setPagina(self, pagina, endereco):
        if endereco >= self.qtPaginas:
            print(f'MemoriaPrincipal: tentativa de acesso a pagina fora do limite. Limite({self.qtPaginas}) Pagina de Acesso ({endereco})' )
        self.__escritas = self.__escritas + 1
        self.__memoria[endereco] = pagina
    
    def getLeituras(self):
        return self.__leituras
    
    def getEscritas(self):
        return self.__escritas

def geraHash(i):
    return int(hashlib.sha256(str(i).encode('ASCII')).hexdigest(), 16) % 10000


def dumpMemorias(memoriaPrincipal, memoriaSecundaria):
    print('\tMemoriaSecundaria\t\tMemoriaPrincipal')
    for i in range(memoriaSecundaria.qtPaginas):
        if i < memoriaPrincipal.qtPaginas:
            print(f'\t{i}:[{memoriaSecundaria.getPagina(i)}]\t[{memoriaPrincipal.getPagina(i)}]:{i}')
        else:
            print(f'\t{i}:[{memoriaSecundaria.getPagina(i)}]')

def pseudonorm(intervalo):
    count = 10
    values =  sum([random.randint(0, intervalo) for x in range(count)])
    return round(values/count)


def testaMapeamento(nEnderecos: int, nPaginasMemoriaPrincipal: int, nPaginasMemoriaSecundaria: int, debug: bool, funcaoMapeamento, funcaoInicializacaoMapeamento):
    random.seed(0)

    memoriaPrincipal = MemoriaPrincipal(nPaginasMemoriaPrincipal)
    memoriaSecundaria = MemoriaSecundaria(nPaginasMemoriaSecundaria)
    nEscritasMemoriaPrincipal = 0

    funcaoInicializacaoMapeamento(memoriaPrincipal, memoriaSecundaria)

    for i in range(nEnderecos):
        endereco = pseudonorm(nPaginasMemoriaSecundaria * 4)

        aux = memoriaPrincipal.getEscritas()
        endMemPrincipal = funcaoMapeamento(memoriaPrincipal, memoriaSecundaria, endereco)
        nEscritasMemoriaPrincipal = nEscritasMemoriaPrincipal + (memoriaPrincipal.getEscritas() - aux)

        pagina = memoriaPrincipal.getPagina(endMemPrincipal)
        byte = pagina[endereco & 3]

        if debug:
            print(f'Endereco gerado: {endereco}')
            print(f'Endereco recebido pela funcao mapeamento: {endMemPrincipal}')
            print(f'Valor na memoriaPrincipal no endereco recebido: {pagina}')
            print(f'Valor esperado no endereco recebido: {geraHash(endereco)}')
            dumpMemorias(memoriaPrincipal, memoriaSecundaria)
            print('Pressione enter para o proximo endereco =)')
            sys.stdin.read(1)
        
        bytepego = memoriaSecundaria.getPagina(endereco >> 2)[endereco & 3]

        if byte != bytepego:
            if not debug:
                dumpMemorias(memoriaPrincipal, memoriaSecundaria)
            print('Sua funcao de mapeamento retornou endereco para uma pagina errada')
            sys.exit(0)
    print(f'Todos os {nEnderecos} enderecos foram gerados. A sua funcao de mapeamento esta corretamente implementada =)')
    print(f'Performance')
    print(f'\tVoce gerou {nEscritasMemoriaPrincipal} escritas na memoriaPrincipal')
    cacheHit = (1 - (nEscritasMemoriaPrincipal / nEnderecos)) * 100
    print(f'\tSua funcao de mapeamento conseguiu atingir o seguinte CACHE HIT: {cacheHit:02f}')