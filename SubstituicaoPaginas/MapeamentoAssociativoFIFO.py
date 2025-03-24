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
indice =0
def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global indice

    tag = endereco >> 5
    ind = (endereco >>2) & 7
    paginaRequisitada = endereco >>2
    conteudoPagina = endereco & 3
    byteRequisitado = endereco & 3

    for i in range(len(tabelaMapeamento)):
        if tabelaMapeamento[i] == paginaRequisitada:
            return i

    for i in range(len(tabelaMapeamento)):
        if tabelaMapeamento[i] == -1:
            pagina = memoriaSecundaria.getPagina(paginaRequisitada)
            memoriaPrincipal.setPagina(pagina, i)
            tabelaMapeamento[i] = paginaRequisitada
            return i
        
    pagina = memoriaSecundaria.getPagina(paginaRequisitada)
    memoriaPrincipal.setPagina(pagina, indice)
    tabelaMapeamento[indice] = paginaRequisitada
    indice = indice +1

    if indice == qtPaginasMemoriaPrincipal:
        indice =0
        return qtPaginasMemoriaPrincipal -1
    
    return indice -1

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    tabelaMapeamento =[]
    for i in range(8):
        tabelaMapeamento.append(-1)

    #executa funcao de mapeamento com 30 enderecos em modo Debug
    testaMapeamento(nEnderecos=30, 
                                nPaginasMemoriaPrincipal=8, 
                                nPaginasMemoriaSecundaria=16, 
                                debug=True, 
                                funcaoMapeamento=mapeamentoAssociativo,
                                funcaoInicializacaoMapeamento=inicializaMapeamento)
    
    indice =0
    tabelaMapeamento =[]
    for i in range(1024):
        tabelaMapeamento.append(-1)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=3000, 
                                nPaginasMemoriaPrincipal=1024, 
                                nPaginasMemoriaSecundaria=4096, 
                                debug=False, 
                                funcaoMapeamento=mapeamentoAssociativo, 
                                funcaoInicializacaoMapeamento=inicializaMapeamento)

