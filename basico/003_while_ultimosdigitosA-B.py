"""Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

"""

N = int(input())

while(N > 0):
    a,b = input("Digite dois números: ").split() #aplica dois valores separados por espaço dentro a variavel a,b | por exemplo, um valor fornecido pelo usuário seja "3 9", o valor "3" vai para a variavel a e o valor "9" vai para a variavel b
    if b == a[len(a)-len(b):len(a)]: #verifica os ultimos valores da variável a é igual a b
        print("encaixa")
    else:
        print("nao encaixa")
    N -= 1