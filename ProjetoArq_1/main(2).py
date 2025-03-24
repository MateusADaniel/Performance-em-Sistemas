import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = False

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    if instrucao == 0x40:
        print('MOV Reg, Byte')
        return 40
    elif instrucao == 0x01:
        print('ADD Reg, Reg')
        return 1
    elif instrucao == 0x10:
        print('INC Reg')
        return 10
    elif instrucao == 0x20:
        print('DEC Reg')
        return 20
    elif instrucao == 0x00:
        print('ADD Reg, Byte')
        return 0
    elif instrucao == 0x30:
        print('SUB Reg, Byte')
        return 30
    elif instrucao == 0x31:
        print('SUB Reg, Reg')
        return 31
    elif instrucao == 0x41:
        print('MOV Reg, Reg')
        return 41
    elif instrucao == 0x70: # no arquivo de memória todas_instrucoes.bin trocar o valor de 0x70 para 0x79
        print('JZ, Byte')
        return 70
    elif instrucao == 0x60:
        print('CMP Reg, Byte')
        return 60
    elif instrucao == 0x61:
        print('CMP Reg, Reg')
        return 61
    elif instrucao == 0x50:
        print('JMP Byte')
        return 50
    
    return -1


def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx
    global registrador_cp
    global flag_zero
    ##MOV REG BYTE
    if idInstrucao == 40:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax = operador2
        elif operador1 == 0x03:
            registrador_bx = operador2
        elif operador1 == 0x04:
            registrador_cx = operador2
        elif operador1 == 0x05:
            registrador_dc = operador2 
    #MOV REG REG
    elif idInstrucao == 41:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax = registrador_ax
            elif operador2 == 0x03:
                registrador_ax = registrador_bx
            elif operador2 == 0x04:
                registrador_ax = registrador_cx
            elif operador2 == 0x05:
                registrador_ax = registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx = registrador_ax
            elif operador2 == 0x03:
                registrador_bx = registrador_bx
            elif operador2 == 0x04:
                registrador_bx = registrador_cx
            elif operador2 == 0x05:
                registrador_bx = registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx = registrador_ax
            elif operador2 == 0x03:
                registrador_cx = registrador_bx
            elif operador2 == 0x04:
                registrador_cx = registrador_cx
            elif operador2 == 0x05:
                registrador_cx = registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx = registrador_ax
            elif operador2 == 0x03:
                registrador_dx = registrador_bx
            elif operador2 == 0x04:
                registrador_dx = registrador_cx
            elif operador2 == 0x05:
                registrador_dx = registrador_dx
    #ADD REG REG
    elif idInstrucao == 1:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax += registrador_ax
            elif operador2 == 0x03:
                registrador_ax += registrador_bx
            elif operador2 == 0x04:
                registrador_ax += registrador_cx
            elif operador2 == 0x05:
                registrador_ax += registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx += registrador_ax
            elif operador2 == 0x03:
                registrador_bx += registrador_bx
            elif operador2 == 0x04:
                registrador_bx += registrador_cx
            elif operador2 == 0x05:
                registrador_bx += registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx += registrador_ax
            elif operador2 == 0x03:
                registrador_cx += registrador_bx
            elif operador2 == 0x04:
                registrador_cx += registrador_cx
            elif operador2 == 0x05:
                registrador_cx += registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx += registrador_ax
            elif operador2 == 0x03:
                registrador_dx += registrador_bx
            elif operador2 == 0x04:
                registrador_dx += registrador_cx
            elif operador2 == 0x05:
                registrador_dx += registrador_dx
    #SUB REG REG
    elif idInstrucao == 31:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax -= registrador_ax
            elif operador2 == 0x03:
                registrador_ax -= registrador_bx
            elif operador2 == 0x04:
                registrador_ax -= registrador_cx
            elif operador2 == 0x05:
                registrador_ax -= registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx -= registrador_ax
            elif operador2 == 0x03:
                registrador_bx -= registrador_bx
            elif operador2 == 0x04:
                registrador_bx -= registrador_cx
            elif operador2 == 0x05:
                registrador_bx -= registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx -= registrador_ax
            elif operador2 == 0x03:
                registrador_cx -= registrador_bx
            elif operador2 == 0x04:
                registrador_cx -= registrador_cx
            elif operador2 == 0x05:
                registrador_cx -= registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx -= registrador_ax
            elif operador2 == 0x03:
                registrador_dx -= registrador_bx
            elif operador2 == 0x04:
                registrador_dx -= registrador_cx
            elif operador2 == 0x05:
                registrador_dx -= registrador_dx
    #ADD REG BYTE
    elif idInstrucao == 0:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax += operador2
        elif operador1 == 0x03:
            registrador_bx += operador2
        elif operador1 == 0x04:
            registrador_cx += operador2
        elif operador1 == 0x05:
            registrador_dx += operador2
    #SUB REG BYTE
    elif idInstrucao == 30:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax -= operador2
        elif operador1 == 0x03:
            registrador_bx -= operador2
        elif operador1 == 0x04:
            registrador_cx -= operador2
        elif operador1 == 0x05:
            registrador_dx -= operador2
    #INC REG
    elif idInstrucao == 10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax += 1
        elif operador1 == 0x03:
            registrador_bx += 1
        elif operador1 == 0x04:
            registrador_cx += 1
        elif operador1 == 0x05:
            registrador_dx += 1
    #DEC REG
    elif idInstrucao == 20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax -= 1
        elif operador1 == 0x03:
            registrador_bx -= 1
        elif operador1 == 0x04:
            registrador_cx -= 1
        elif operador1 == 0x05:
            registrador_dx -= 1
    #JZ BYTE
    elif idInstrucao == 70:
        operador1 = memoria.getValorMemoria(registrador_cp+1)
        if flag_zero == True:
            registrador_cp = operador1



    #CMP REG BYTE
    elif idInstrucao == 60:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if registrador_ax == operador2:
                flag_zero = True
        elif operador1 == 0x03:
            if registrador_bx == operador2:
                flag_zero = True
        elif operador1 == 0x04:
            if registrador_cx == operador2:
                flag_zero = True
        elif operador1 == 0x05:
            if registrador_dx == operador2:
                flag_zero = True
    #CMP REG REG
    elif idInstrucao == 61:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                if registrador_ax == registrador_ax:
                    flag_zero = True
            elif operador2 == 0x03:
                if registrador_ax == registrador_bx:
                    flag_zero = True
            elif operador2 == 0x04:
                if registrador_ax == registrador_cx:
                    flag_zero = True
            elif operador2 == 0x05:
                if registrador_ax == registrador_dx:
                    flag_zero = True
        elif operador1 == 0x03:
            if operador2 == 0x02:
                if registrador_bx == registrador_ax:
                    flag_zero = True
            elif operador2 == 0x03:
                if registrador_bx == registrador_bx:
                    flag_zero = True
            elif operador2 == 0x04:
                if registrador_bx == registrador_cx:
                    flag_zero = True
            elif operador2 == 0x05:
                if registrador_bx == registrador_dx:
                    flag_zero = True
        elif operador1 == 0x04:
            if operador2 == 0x02:
                if registrador_cx == registrador_ax:
                    flag_zero = True
            elif operador2 == 0x03:
                if registrador_cx == registrador_bx:
                    flag_zero = True
            elif operador2 == 0x04:
                if registrador_cx == registrador_cx:
                    flag_zero = True
            elif operador2 == 0x05:
                if registrador_cx == registrador_dx:
                    flag_zero = True
        elif operador1 == 0x05:
            if operador2 == 0x02:
                if registrador_dx == registrador_ax:
                    flag_zero = True
            elif operador2 == 0x03:
                if registrador_dx == registrador_bx:
                    flag_zero = True
            elif operador2 == 0x04:
                if registrador_dx == registrador_cx:
                    flag_zero = True
            elif operador2 == 0x05:
                if registrador_dx == registrador_dx:
                    flag_zero = True
    if idInstrucao == 50:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        registrador_cp = operador1


def calcularProximaInstrucao(idInstrucao):
    global flag_zero
    global registrador_cp


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
        if flag_zero == False:
            registrador_cp += 2
        else:
            flag_zero = False
    elif idInstrucao == 60:
        registrador_cp += 3
    elif idInstrucao == 61:
        registrador_cp += 3
    if CPU_DEBUG == True:
        print(f'mudando registrador_cp para {registrador_cp}')


def dumpRegistradores():
    global registrador_ax, registrador_bx, registrador_cx, registrador_dx, registrador_cp
    if CPU_DEBUG == True:
        if idInstrucao == 40:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  print(f'Movendo {operador2} para registrador_ax')
              elif operador1 == 0x03:
                  print(f'Movendo {operador2} para registrador_bx')
              elif operador1 == 0x04:
                  print(f'Movendo {operador2} para registrador_cx')
              elif operador1 == 0x05:
                  print(f'Movendo {operador2} para registrador_dx')
        elif idInstrucao == 1:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  if operador2 == 0x02:
                      print(f'somando registrador_ax com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'somando registrador_ax com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'somando registrador_ax com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'somando registrador_ax com registrador_dx') 
              elif operador1 == 0x03:
                  if operador2 == 0x02:
                      print(f'somando registrador_bx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'somando registrador_bx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'somando registrador_bx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'somando registrador_bx com registrador_dx') 
              elif operador1 == 0x04:
                  if operador2 == 0x02:
                      print(f'somando registrador_cx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'somando registrador_cx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'somando registrador_cx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'somando registrador_cx com registrador_dx') 
              elif operador1 == 0x05:
                  if operador2 == 0x02:
                      print(f'somando registrador_dx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'somando registrador_dx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'somando registrador_dx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'somando registrador_dx com registrador_dx') 
        elif idInstrucao == 10:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              if operador1 == 0x02:
                  print(f'incrementando 1 no registrador_ax')
              elif operador1 == 0x03:
                  print(f'incrementando 1 no registrador_bx')
              elif operador1 == 0x04:
                  print(f'incrementando 1 no registrador_cx')
              elif operador1 == 0x05:
                  print(f'incrementando 1 no registrador_dx')
        elif idInstrucao == 20:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              if operador1 == 0x02:
                  print(f'decrementando 1 no registrador_ax')
              elif operador1 == 0x03:
                  print(f'decrementando 1 no registrador_bx')
              elif operador1 == 0x04:
                  print(f'decrementando 1 no registrador_cx')
              elif operador1 == 0x05:
                  print(f'decrementando 1 no registrador_dx')
        elif idInstrucao == 0:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  print(f'somando {operador2} no regsitrador_ax')
              elif operador1 == 0x03:
                  print(f'somando {operador2} no regsitrador_bx')
              elif operador1 == 0x04:
                  print(f'somando {operador2} no regsitrador_cx')
              elif operador1 == 0x05:
                  print(f'somando {operador2} no regsitrador_dx')
        elif idInstrucao == 30:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  print(f'subtraindo {operador2} no regsitrador_ax')
              elif operador1 == 0x03:
                  print(f'subtraindo {operador2} no regsitrador_bx')
              elif operador1 == 0x04:
                  print(f'subtraindo {operador2} no regsitrador_cx')
              elif operador1 == 0x05:
                  print(f'subtraindo {operador2} no regsitrador_dx')
        elif idInstrucao == 31:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  if operador2 == 0x02:
                      print(f'subtraindo registrador_ax com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'subtraindo registrador_ax com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'subtraindo registrador_ax com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'subtraindo registrador_ax com registrador_dx') 
              elif operador1 == 0x03:
                  if operador2 == 0x02:
                      print(f'subtraindo registrador_bx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'subtraindo registrador_bx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'subtraindo registrador_bx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'subtraindo registrador_bx com registrador_dx') 
              elif operador1 == 0x04:
                  if operador2 == 0x02:
                      print(f'subtraindo registrador_cx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'subtraindo registrador_cx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'subtraindo registrador_cx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'subtraindo registrador_cx com registrador_dx') 
              elif operador1 == 0x05:
                  if operador2 == 0x02:
                      print(f'subtraindo registrador_dx com registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'subtraindo registrador_dx com registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'subtraindo registrador_dx com registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'subtraindo registrador_dx com registrador_dx') 
        elif idInstrucao == 41:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  if operador2 == 0x02:
                      print(f'movendo registrador_ax para registrador_ax') 
                  elif operador2 == 0x03:
                      print(f'movendo registrador_bx para registrador_ax') 
                  elif operador2 == 0x04:
                      print(f'movendo registrador_cx para registrador_ax') 
                  elif operador2 == 0x05:
                      print(f'movendo registrador_dx para registrador_ax') 
              elif operador1 == 0x03:
                  if operador2 == 0x02:
                      print(f'movendo registrador_ax para registrador_bx') 
                  elif operador2 == 0x03:
                      print(f'movendo registrador_bx para registrador_bx') 
                  elif operador2 == 0x04:
                      print(f'movendo registrador_cx para registrador_bx') 
                  elif operador2 == 0x05:
                      print(f'movendo registrador_dx para registrador_bx') 
              elif operador1 == 0x04:
                  if operador2 == 0x02:
                      print(f'movendo registrador_ax para registrador_cx') 
                  elif operador2 == 0x03:
                      print(f'movendo registrador_bx para registrador_cx') 
                  elif operador2 == 0x04:
                      print(f'movendo registrador_cx para registrador_cx') 
                  elif operador2 == 0x05:
                      print(f'movendo registrador_dx para registrador_cx') 
              elif operador1 == 0x05:
                  if operador2 == 0x02:
                      print(f'movendo registrador_ax para registrador_dx') 
                  elif operador2 == 0x03:
                      print(f'movendo registrador_bx para registrador_dx') 
                  elif operador2 == 0x04:
                      print(f'movendo registrador_cx para registrador_dx') 
                  elif operador2 == 0x05:
                      print(f'movendo registrador_dx para registrador_dx') 
        elif idInstrucao == 70:
              operador1 = memoria.getValorMemoria(registrador_cp+1)
              if flag_zero == True:
                  print(f'modificando o registrador_cp para {operador1}')
              else:
                  print(f'flag_zero igual FALSE')
        elif idInstrucao == 60:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  print(f'comparando registrador_ax com {operador2}')
              elif operador1 == 0x03:
                  print(f'comparando registrador_bx com {operador2}')
              elif operador1 == 0x04:
                  print(f'comparando registrador_cx com {operador2}')
              elif operador1 == 0x05:
                  print(f'comparando registrador_dx com {operador2}')
          #CMP REG REG
        elif idInstrucao == 61:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              operador2 = memoria.getValorMemoria(registrador_cp + 2)
              if operador1 == 0x02:
                  if operador2 == 0x02:
                      print('comparando registrador_ax com registrador_ax')
                  elif operador2 == 0x03:
                      print('comparando registrador_ax com registrador_bx')
                  elif operador2 == 0x04:
                      print('comparando registrador_ax com registrador_cx')
                  elif operador2 == 0x05:
                      print('comparando registrador_ax com registrador_dx')
              elif operador1 == 0x03:
                  if operador2 == 0x02:
                      print('comparando registrador_bx com registrador_ax')
                  elif operador2 == 0x03:
                      print('comparando registrador_bx com registrador_bx')
                  elif operador2 == 0x04:
                      print('comparando registrador_bx com registrador_cx')
                  elif operador2 == 0x05:
                      print('comparando registrador_bx com registrador_dx')
              elif operador1 == 0x04:
                  if operador2 == 0x02:
                      print('comparando registrador_cx com registrador_ax')
                  elif operador2 == 0x03:
                      print('comparando registrador_cx com registrador_bx')
                  elif operador2 == 0x04:
                      print('comparando registrador_cx com registrador_cx')
                  elif operador2 == 0x05:
                      print('comparando registrador_cx com registrador_dx')
              elif operador1 == 0x05:
                  if operador2 == 0x02:
                      print('comparando registrador_dx com registrador_ax')
                  elif operador2 == 0x03:
                      print('comparando registrador_dx com registrador_bx')
                  elif operador2 == 0x04:
                      print('comparando registrador_dx com registrador_cx')
                  elif operador2 == 0x05:
                      print('comparando registrador_dx com registrador_dx')
        if idInstrucao == 50:
              operador1 = memoria.getValorMemoria(registrador_cp + 1)
              print(f'modificando registrador_cp para região {operador1}')
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
    
