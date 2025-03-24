import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso de todos enderecos na memoria principal

#    tente otimizar o seu mecanismo de mapeamento
#    tente otimizar o seu mecanismo de substituicao
tabelaMapeamento = []

def mapeamentoCustomizado(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global tabelaMapeamento
    tag = endereco >> 5
    ind = endereco & 12
    print(tag, ind)
    paginaRequisitada = ind 

    pagina = memoriaSecundaria.getPagina(paginaRequisitada)
    memoriaPrincipal.setPagina(pagina, 0)
    # se ja foi mapeado, retoranr o endereco
    for i in range(len(tabelaMapeamento)):
        if tabelaMapeamento[i] == paginaRequisitada:
            return i
        
        #senao, mapear, e retornar o endereco
    pagina = memoriaSecundaria.getPagina(paginaRequisitada)
    for i in range(len(tabelaMapeamento)):
        if tabelaMapeamento[i] == -1:
            memoriaPrincipal.setPagina(pagina, i)
            tabelaMapeamento[i] = paginaRequisitada
            return i
        
    #memoria princial cheia
    tabelaMapeamento[0] = paginaRequisitada
    memoriaPrincipal.setPagina(pagina, 0)

    return 0

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    for i in range(8):
        tabelaMapeamento.append(-1)

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                                nPaginasMemoriaPrincipal=8, 
                                nPaginasMemoriaSecundaria=16, 
                                debug=True, 
                                funcaoMapeamento=mapeamentoCustomizado,
                                funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=300, 
                                nPaginasMemoriaPrincipal=128, 
                                nPaginasMemoriaSecundaria=512, 
                                debug=False, 
                                funcaoMapeamento=mapeamentoCustomizado, 
                                funcaoInicializacaoMapeamento=inicializaMapeamento)

