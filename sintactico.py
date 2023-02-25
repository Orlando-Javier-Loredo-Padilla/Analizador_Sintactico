# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:24:13 2023

@author: Orlando
"""

from operator import is_
from pila import Stack,  Stack2, Stack3, Stack4

#Valores
ERROR = -1
IDENTIFICADOR = 0
SIMBOLO = 1
SIGNOPESOS = 2
E = 3
INICIAL = 5


def primer(texto):
    print(texto)
    print ("Pila", end ="")
    print("                    Entrada")
    print("2 0                     ", end ="")
    pila = Stack()
    entrada = Stack2()

    estado = INICIAL
    d = 2
    d2= 2
    j = 0
    i = 0
    lexema = ""
        
    #Entrada
    while(j<len(texto)):
        c2 = texto[j]
        if(estado == INICIAL):
            if (es_Letra(c2) or c2 == '_'): 
                estado = IDENTIFICADOR
                lexema += c2
            elif (c2 == '+'):        
                entrada.push(1)
                d2+=1
                estado = INICIAL
                lexema = ""
            elif (c2 == '$'):
                entrada.push(2)
            else:
                print("ERROR")

        elif(estado == IDENTIFICADOR):
            if(es_Letra(c2) or isReal(c2) or c2 == '_'):
                estado = IDENTIFICADOR
                lexema += c2
                
            else:
                entrada.push(0)
                d2 += 1
                estado = INICIAL
                lexema = ""
                j -= 1    
        j += 1
        
    entrada.mostrar_entrada()  
    
    #Pila
    while(i<len(texto)):
        c = texto[i]
        if(estado == INICIAL):
            if (es_Letra(c) or c == '_'): 
                estado = IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(SIMBOLO)
                pila.push(d)
                d+=1
                estado = INICIAL
              
                lexema = ""
                pila.mostrarPila()
                entrada.pop()
                entrada.mostrar_entrada()
                
                
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
                entrada.pop()
                entrada.mostrar_entrada()
            
            else:
                print("ERROR")

        elif(estado == IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = IDENTIFICADOR
                lexema += c
                
            else:
                pila.push(IDENTIFICADOR)
                pila.push(d)
                d += 1
                estado = INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila() 
                entrada.pop()
                entrada.mostrar_entrada()

                
        i += 1
    

def segundo(texto):    
    print(texto)
    print ("Pila", end ="")
    print("                                    Entrada")
    print("2 0                                       ", end ="")
    pila = Stack3()
    entrada = Stack4()
    estado = INICIAL
    d3 = 2
    d4 = 3
    d33 = 2
    d44 = 3
    j = 0
    i = 0
    lexema = ""
    
    #entrada
    while(j<len(texto)):
        c2 = texto[j]
        if(estado == INICIAL):
            if (es_Letra(c2) or c2 == '_'): 
                estado = IDENTIFICADOR
                lexema += c2
            elif (c2 == '+'):        
                entrada.push(1)
                d3+=1
                estado = INICIAL
                lexema = ""
            elif (c2 == '$'):
                entrada.push(2)
            else:
                print("ERROR")

        elif(estado == IDENTIFICADOR):
            if(es_Letra(c2) or isReal(c2) or c2 == '_'):
                estado = IDENTIFICADOR
                lexema += c2
            else:
                entrada.push(0)
                d3 += 1
                estado = INICIAL
                lexema = ""
                j -= 1    
        j += 1
        
    entrada.mostrar_entrada()        
    i = 0
    
    while(i<len(texto)):
        c = texto[i]

        if(estado == INICIAL):
            if (es_Letra(c) or c == '_'): 
                estado = IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(SIMBOLO)
                pila.push(d44)
                estado = INICIAL
                lexema = ""
                pila.mostrarPila()
                entrada.pop()
                entrada.mostrar_entrada()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
                entrada.pop()
                entrada.mostrar_entrada()
            else:
                print("ERROR")

        elif(estado == IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = IDENTIFICADOR
                lexema += c
            else:
                pila.push(IDENTIFICADOR)
                pila.push(d33)
                estado = INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
                entrada.pop()
                entrada.mostrar_entrada()
        i += 1   

def isReal(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return True
    else:
        return False

def es_Letra(c):
    if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
        return True
    else:
        return False

print("Ejercicio 1: ")
primer("hola+mundo$")
print()
print("Ejercicio 2: ")
segundo("a+b+c+d+e+f$")

