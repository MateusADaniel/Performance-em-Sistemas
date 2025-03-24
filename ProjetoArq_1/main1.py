import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin') -NECESSARIO MUDAR A INTRUCAO DE JZ PARA 0x79 
#                                                                 DEVIDO A COMO ESTA NO CODIGO .BIN DO PROF.
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)

    if instrucao == 0x40:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução MOV Reg e Byte')
        return 40
    elif instrucao == 0x01:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução ADD Reg e Reg')
        return 1
    elif instrucao == 0x10:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução INC Reg')
        return 10
    elif instrucao == 0x20:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução DEC Reg')
        return 20
    elif instrucao == 0x00:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução ADD Reg e Byte')
        return 0
    elif instrucao == 0x30:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução SUB Reg e Byte')
        return 30
    elif instrucao == 0x31:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução SUB Reg e Reg')
        return 31
    elif instrucao == 0x41:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução MOV Reg e Reg')
        return 41
    elif instrucao == 0x70:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução JZ Byte')
        return 70
    elif instrucao == 0x60:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução CMP Reg e Byte')
        return 60
    elif instrucao == 0x61:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução CMP Reg e Reg')
        return 61
    elif instrucao == 0x50:
        print(f'buscarEDecodificarInstrucao(n:{instrucao}): instrução JMP Byte')
        return 50
    
    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx
    global registrador_cp
    global flag_zero

    if idInstrucao == 40:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax = operador2
            print(f'lerOperadoresExecutarInstrucao: atribuindo {operador2} em AX')
        elif operador1 == 0x03:
            registrador_bx = operador2
            print(f'lerOperadoresExecutarInstrucao: atribuindo {operador2} em BX')
        elif operador1 == 0x04:
            registrador_cx = operador2
            print(f'lerOperadoresExecutarInstrucao: atribuindo {operador2} em CX')
        elif operador1 == 0x05:
            registrador_dx = operador2
            print(f'lerOperadoresExecutarInstrucao: atribuindo {operador2} em DX')

    elif idInstrucao == 1:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax += registrador_ax
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_ax} em AX')
            elif operador2 == 0x03:
                registrador_ax += registrador_bx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_bx} em AX')
            elif operador2 == 0x04:
                registrador_ax += registrador_cx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_cx} em AX')
            elif operador2 == 0x05:
                registrador_ax += registrador_dx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_dx} em AX')
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx += registrador_ax
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_ax} em BX')
            elif operador2 == 0x03:
                registrador_bx += registrador_bx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_bx} em BX')
            elif operador2 == 0x04:
                registrador_bx += registrador_cx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_cx} em BX')
            elif operador2 == 0x05:
                registrador_bx += registrador_dx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_dx} em BX')
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx += registrador_ax
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_ax} em CX')
            elif operador2 == 0x03:
                registrador_cx += registrador_bx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_bx} em CX')
            elif operador2 == 0x04:
                registrador_cx += registrador_cx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_cx} em CX')
            elif operador2 == 0x05:
                registrador_cx += registrador_dx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_dx} em CX')
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx += registrador_ax
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_ax} em DX')
            elif operador2 == 0x03:
                registrador_dx += registrador_bx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_bx} em DX')
            elif operador2 == 0x04:
                registrador_dx += registrador_cx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_cx} em DX')
            elif operador2 == 0x05:
                registrador_dx += registrador_dx
                print(f'lerOperadoresExecutarInstrucao: somando {registrador_dx} em DX')

    elif idInstrucao == 10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax += 1
            print(f'lerOperadoresExecutarInstrucao: incrementando 1 em AX')
        elif operador1 == 0x03:
            registrador_bx += 1
            print(f'lerOperadoresExecutarInstrucao: incrementando 1 em BX')
        elif operador1 == 0x04:
            registrador_cx += 1
            print(f'lerOperadoresExecutarInstrucao: incrementando 1 em CX')
        elif operador1 == 0x05:
            registrador_dx += 1
            print(f'lerOperadoresExecutarInstrucao: incrementando 1 em DX')
                
    elif idInstrucao == 20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax -= 1
            print(f'lerOperadoresExecutarInstrucao: decrementando 1 em AX')
        elif operador1 == 0x03:
            registrador_bx -= 1
            print(f'lerOperadoresExecutarInstrucao: decrementando 1 em BX')
        elif operador1 == 0x04:
            registrador_cx -= 1
            print(f'lerOperadoresExecutarInstrucao: decrementando 1 em CX')
        elif operador1 == 0x05:
            registrador_dx -= 1
            print(f'lerOperadoresExecutarInstrucao: decrementando 1 em DX')

    elif idInstrucao == 0:
        operador1 = memoria.getValorMemoria(registrador_cp + 1) #reg
        operador2 = memoria.getValorMemoria(registrador_cp + 2) #byte
        if operador1 == 0x02:
            registrador_ax += operador2
            print(f'lerOperadoresExecutarInstrucao: somando {operador2} em AX')
        elif operador1 == 0x03:
            registrador_bx += operador2
            print(f'lerOperadoresExecutarInstrucao: somando {operador2} em BX')
        elif operador1 == 0x04:
            registrador_cx += operador2
            print(f'lerOperadoresExecutarInstrucao: somando {operador2} em CX')
        elif operador1 == 0x05:
            registrador_dx += operador2
            print(f'lerOperadoresExecutarInstrucao: somando {operador2} em DX')

    elif idInstrucao == 30:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax -= operador2
            print(f'lerOperadoresExecutarInstrucao: subtrair {operador2} em AX')
        elif operador1 == 0x03:
            registrador_bx -= operador2
            print(f'lerOperadoresExecutarInstrucao: subtrair {operador2} em BX')
        elif operador1 == 0x04:
            registrador_cx -= operador2
            print(f'lerOperadoresExecutarInstrucao: subtrair {operador2} em CX')
        elif operador1 == 0x05:
            registrador_dx -= operador2
            print(f'lerOperadoresExecutarInstrucao: subtrair {operador2} em DX')

    elif idInstrucao == 31:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax -= registrador_ax
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_ax} em AX')
            elif operador2 == 0x03:
                registrador_ax -= registrador_bx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_bx} em AX')
            elif operador2 == 0x04:
                registrador_ax -= registrador_cx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_cx} em AX')
            elif operador2 == 0x05:
                registrador_ax -= registrador_dx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_dx} em AX')
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx -= registrador_ax
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_ax} em BX')
            elif operador2 == 0x03:
                registrador_bx -= registrador_bx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_bx} em BX')
            elif operador2 == 0x04:
                registrador_bx -= registrador_cx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_cx} em BX')
            elif operador2 == 0x05:
                registrador_bx -= registrador_dx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_dx} em BX')
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx -= registrador_ax
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_ax} em CX')
            elif operador2 == 0x03:
                registrador_cx -= registrador_bx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_bx} em CX')
            elif operador2 == 0x04:
                registrador_cx -= registrador_cx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_cx} em CX')
            elif operador2 == 0x05:
                registrador_cx -= registrador_dx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_dx} em CX')
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx -= registrador_ax
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_ax} em DX')
            elif operador2 == 0x03:
                registrador_dx -= registrador_bx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_bx} em DX')
            elif operador2 == 0x04:
                registrador_dx -= registrador_cx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_cx} em DX')
            elif operador2 == 0x05:
                registrador_dx -= registrador_dx
                print(f'lerOperadoresExecutarInstrucao: subtrair {registrador_dx} em DX')

    elif idInstrucao == 41:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax = registrador_ax
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_ax} em AX')
            elif operador2 == 0x03:
                registrador_ax = registrador_bx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_bx} em AX')
            elif operador2 == 0x04:
                registrador_ax = registrador_cx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_cx} em AX')
            elif operador2 == 0x05:
                registrador_ax = registrador_dx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_dx} em AX')
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx = registrador_ax
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_ax} em BX')
            elif operador2 == 0x03:
                registrador_bx = registrador_bx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_bx} em BX')
            elif operador2 == 0x04:
                registrador_bx = registrador_cx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_cx} em BX')
            elif operador2 == 0x05:
                registrador_bx = registrador_dx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_dx} em BX')
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx = registrador_ax
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_ax} em CX')
            elif operador2 == 0x03:
                registrador_cx = registrador_bx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_bx} em CX')
            elif operador2 == 0x04:
                registrador_cx = registrador_cx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_cx} em CX')
            elif operador2 == 0x05:
                registrador_cx = registrador_dx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_dx} em CX')
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx = registrador_ax
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_ax} em DX')
            elif operador2 == 0x03:
                registrador_dx = registrador_bx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_bx} em DX')
            elif operador2 == 0x04:
                registrador_dx = registrador_cx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_cx} em DX')
            elif operador2 == 0x05:
                registrador_dx = registrador_dx
                print(f'lerOperadoresExecutarInstrucao: atribuindo {registrador_dx} em DX')

    elif idInstrucao == 70:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if flag_zero == True:
            registrador_cp = operador1
            print(f'lerOperadoresExecutarInstrucao: Salta execução da CPU para {operador1}, ZF = {flag_zero}')
        print(f'lerOperadoresExecutarInstrucao: Não Salta execução da CPU, ZF = {flag_zero}')

    elif idInstrucao == 60:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if registrador_ax == operador2:
                flag_zero = True
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {operador2}, ZF = {flag_zero}')
            print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {operador2}, ZF = {flag_zero}')
        elif operador1 == 0x03:
            if registrador_bx == operador2:
                flag_zero = True
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {operador2}, ZF = {flag_zero}')
            print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {operador2}, ZF = {flag_zero}')
        elif operador1 == 0x04:
            if registrador_cx == operador2:
                flag_zero = True
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {operador2}, ZF = {flag_zero}')
            print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {operador2}, ZF = {flag_zero}')
        elif operador1 == 0x05:
            if registrador_dx == operador2:
                flag_zero = True
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {operador2}, ZF = {flag_zero}')
            print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {operador2}, ZF = {flag_zero}')

    elif idInstrucao == 61:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                if registrador_ax == registrador_ax:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_ax}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_ax}, ZF = {flag_zero}')
            elif operador2 == 0x03:
                if registrador_ax == registrador_bx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_bx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_bx}, ZF = {flag_zero}')
            elif operador2 == 0x04:
                if registrador_ax == registrador_cx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_cx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_cx}, ZF = {flag_zero}')
            elif operador2 == 0x05:
                if registrador_ax == registrador_dx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_dx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_ax} com {registrador_dx}, ZF = {flag_zero}')
        elif operador1 == 0x03:
            if operador2 == 0x02:
                if registrador_bx == registrador_ax:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_ax}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_ax}, ZF = {flag_zero}')
            elif operador2 == 0x03:
                if registrador_bx == registrador_bx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_bx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_bx}, ZF = {flag_zero}')
            elif operador2 == 0x04:
                if registrador_bx == registrador_cx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_cx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_cx}, ZF = {flag_zero}')
            elif operador2 == 0x05:
                if registrador_bx == registrador_dx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_dx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_bx} com {registrador_dx}, ZF = {flag_zero}')
        elif operador1 == 0x04:
            if operador2 == 0x02:
                if registrador_cx == registrador_ax:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_ax}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_ax}, ZF = {flag_zero}')
            elif operador2 == 0x03:
                if registrador_cx == registrador_bx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_bx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_bx}, ZF = {flag_zero}')
            elif operador2 == 0x04:
                if registrador_cx == registrador_cx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_cx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_cx}, ZF = {flag_zero}')
            elif operador2 == 0x05:
                if registrador_cx == registrador_dx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_dx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_cx} com {registrador_dx}, ZF = {flag_zero}')
        elif operador1 == 0x05:
            if operador2 == 0x02:
                if registrador_dx == registrador_ax:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_ax}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_ax}, ZF = {flag_zero}')
            elif operador2 == 0x03:
                if registrador_dx == registrador_bx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_bx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_bx}, ZF = {flag_zero}')
            elif operador2 == 0x04:
                if registrador_dx == registrador_cx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_cx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_cx}, ZF = {flag_zero}')
            elif operador2 == 0x05:
                if registrador_dx == registrador_dx:
                    flag_zero = True
                    print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_dx}, ZF = {flag_zero}')
                print(f'lerOperadoresExecutarInstrucao: Comparando valor {registrador_dx} com {registrador_dx}, ZF = {flag_zero}')
                    
    elif idInstrucao == 50:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        registrador_cp = operador1
        print(f'lerOperadoresExecutarInstrucao: Salta execução da CPU para {operador1}')

def calcularProximaInstrucao(idInstrucao):
    global registrador_cp
    global flag_zero
    if idInstrucao == 40:
        registrador_cp += 3
    elif idInstrucao == 1:
        registrador_cp += 3
    elif idInstrucao == 10:
        registrador_cp += 2
    elif idInstrucao == 20:
        registrador_cp += 2
    elif idInstrucao == 0:
        registrador_cp += 3
    elif idInstrucao == 30:
        registrador_cp += 3
    elif idInstrucao == 31:
        registrador_cp += 3
    elif idInstrucao == 41:
        registrador_cp += 3
    elif idInstrucao == 70:
        if flag_zero == True:
            flag_zero = False
        else: registrador_cp += 2
    elif idInstrucao == 60:
        registrador_cp += 3
    elif idInstrucao == 61:
        registrador_cp += 3
    print(f'calcularProximaInstrucao: mudando CP para {registrador_cp}')

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
    
