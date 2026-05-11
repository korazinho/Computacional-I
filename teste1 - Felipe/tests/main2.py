"""
Programa main
Descrição: Esse programa une os modulos de entrada e saídas, afim de criar uma calculadora funcional que só termina de calcular com a palavra "off".
Autor: Felipe Corá
Data 11/05/24
Versão 0.0.1
"""


def main ():
    import es
    import operações as oper

    
    #Alocação de memória
    entrada = ""
    entrada2 = ""
    operador = ""
    resultado = None
    parcela = 0.0
    parcela2 = 0.0


    
    while True:

        #ENtrada de dados
        if resultado is None:
           entrada = input("\nDigite a parcela ou 'OFF' para resetar a memória.")
            
            if entrada.upper() == "off":
                print("\nencerrando atividade")
                break

            parcela1 = es.entradadados(entrada):
        else:
            parcela = resultado
            operador = input("\n Indique a operação, operadores válidos: +, -, * e /: ")
            if operador.upper == "off":
                print("\nencerrando atividade")
                break
            entrada2 = ("\nDigite a parcela ou 'off' para resetar a memória.")
            if entrada2 == "off":
                print("\nencerrando atividade")
                 break
            parcela2 = es.entradadados(entrada2):



            #Processamento de dados
            if operador == "+":
                resultado = oper.soma(parcela,parcela2)
            elif operador == "-":
                resultado = oper.sub(parcela,parcela2)
            elif operador == "*":
                resultado = oper.mult(parcela,parcela2)
            elif operador == "/":
                resultado == oper.div(parcela,parcela2)
            else:
                print(f" operador invalido, a memória é {resultado}".)

            #saída de dados
            print(f"\n O resultado da operação {parcela} {operador} {parcela2} = {resultado}")
            if resultado == "Não é possivél dividir por zero":
                resultado == parcela

    

if __name__   == "__main__":
    main()
                



            
                
    