import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
#memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    if instrucao == 0x40:
        print('MOV Reg, Byte')

    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    print ('Implementar a lerOperadoresExecutarInstrucao')

def calcularProximaInstrucao(idInstrucao):
    print ('Implementar a calcularProximaInstrucao')

def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
