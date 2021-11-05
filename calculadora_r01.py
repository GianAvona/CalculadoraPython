# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:24:51 2021

@data:   05/11/2021

@author: Gianfranco Avona
"""

"""
# -------- DESCRIÇÃO DO ALGORITMO -------- #
    - Calculadora simples, desenvolvida para colocar os conteúdos básicos 
      da linguagem Python e sua sintaxe em prática.
    - Nela você entra com dois valores, e escolhe a operação que deseja afetuar
      em uma interface gerada pelo programa para recolher os dados do usuário.     
"""
valor = 0
qtde = 0
resultados = {qtde: valor}

def begin():    
    while(1):
        
        print("")
        print("Quer fazer algum cálculo? ")
        print('1- SIM       ||      2- NÃO')
        entrada = int(input())
        
        if entrada == 1:    
                operacao = 0               
                print("Qual operação matemática? ")
                print('1- Adição       ||      2- Subtração       ||      3- Multiplicação       ||      4- Divisão       ||      5- SAIR')
                op = int(input())     
                print('')
                if (op >= 1 and op <= 4):
                    
                #inputs do usuário convertidos de string -> float
                    num_1 = float(input("Digite o 1º número: "))
                    num_2 = float(input("Digite o 2º número: ")) 
                    print("")
                    print("")
                    if op == 1:
                        operacao = operacao + 1
                        print("")
                        print(" --- Soma --- ")
                        soma = num_1 + num_2
                        print(num_1, "+", num_2, "=", soma)
                        resultados[operacao] = soma
                        begin()   
                        print("")
                        
                    if op == 2:
                        print("")
                        print(" --- Subtração --- ")
                        subt = num_1 - num_2
                        print(num_1, "-", num_2, "=", subt)
                        resultados[operacao] = subt
                        begin()   
                        print("")
                        
                    if op == 3:
                        print("")
                        print(" --- Multiplicação --- ")
                        mult = num_1 * num_2
                        print(num_1, "*", num_2, "=", mult)  
                        resultados[operacao] = mult
                        begin()   
                        print("")
                        
                    if op == 4:
                        print("")
                        print(" --- Divisão --- ")
                        div = num_1 / num_2
                        print(num_1, "/", num_2, "=", div)
                        #resultados[qtde] = div
                        begin()   
                        print("")
                        
                if op == 5:
                        print("Resultados acumulados: ", resultados)
                        print('Saindo')                       
                        break
                #else das operações matemáticas
                else: 
                    print('Entrada inválida')
                    begin()   
        #else da entrada 1 ou 2
        else: 
             print('Obrigado! Volte quando precisar')             
             break

begin()  
        
