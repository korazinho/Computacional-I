"""
Programa main
Descrição: Esse programa une os modulos de entrada e saídas, afim de criar uma calculadora funcional que só termina de calcular com a palavra "off".
Autor: Felipe Corá
Data 11/05/24
Versão 1.0.0
"""

def main():
    import es
    import operacoes as oper


    #Alocação de memoria
    entrada = ""
    entrada2 = ""
    operador = ""
    resultado = None
    parcela1 = 0.0
    parcela2 = 0.0

    while True:
        
        #Entrada de dados
        if resultado is None:
            entrada = input("\nDigite um numero ou digite FIM para finalizar: ")
            
            if entrada == "FIM":
                print("\nEncerrando atividade")
                break
                
            parcela1 = es.entradadados(entrada)

        else:
            parcela1 = resultado

        operador = input("\nDigite a operação que deseja, operadores validos: +, -, * e /: ")
        if operador == "FIM":
            print("\nEncerrando atividade")
            break

        entrada2 = input("\nDigite um numero ou digite off para finalizar: ")
        if entrada2 == "FIM":
                print("\nEncerrando atividade")
                break
        parcela2 = es.entradadados(entrada2)



        #Processamento de dados
        if operador == "+":
            resultado = oper.soma(parcela1,parcela2)
        elif operador == "-":
            resultado = oper.sub(parcela1,parcela2)
        elif operador == "*":
            resultado = oper.mult(parcela1,parcela2)
        elif operador == "/":
            resultado = oper.div(parcela1,parcela2)
        else:
            print(f"\nO operador '{operador}' é  invalido.")
            resultado = None
            continue


        #Saida de dados
        print(f" O resultado da operação {parcela1} {operador} {parcela2} = {resultado}!")
        if resultado == "Não é possivél dividir por zero":
            resultado = parcela1

if __name__ == "__main__":
    main()

        