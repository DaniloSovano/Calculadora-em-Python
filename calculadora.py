import matplotlib.pyplot as plt
import numpy as np

def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 14
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    print(" " + "_" * maximoCaracteresPorLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maximoCaracteresPorLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " +
              linha.center(maximoCaracteresPorLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " *
              maximoCaracteresPorLinha + padding * " " + "|")
    print("|" + "_" * maximoCaracteresPorLinha + 2 * padding * "_" + "|")
    
calculator = """
 _________________
|  _____________  |
| |_CALCULADORA_| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """
print(calculator)


def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    sub = a-b
    return sub


def multiplicacao(a, b):
    mult = a * b
    return mult


def divisao(a, b):
    div = a/b
    return div


def linear(x, a, b):
    lin = (a * x) + b
    return lin

def plot_linear(x,a,b):
    axisx = np.linspace(-10,10,100)
    axisy = linear(axisx, a , b)
    plt.plot(axisx,axisy, )
    plt.title(f'Grafico da função linear {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def exponencial(a, x):
    exp = a ** x
    return exp


def plot_exponencial(num1, num2):
    x = np.linspace(-10, 10, 100)
    y = exponencial(num1, x)
    plt.plot(x, y)
    plt.title(f'Gráfico da função exponencial: {num1}^{num2}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def funcao_quadratica(x, a, b, c):
    quad = a * x ** 2 + b * x + c
    return quad 

def calcular_raizes(a, b, c):
      delta = b**2 - 4*a*c
      
      if delta > 0:
        raiz1 = (-b + delta ** 0.5) / (2*a)
        raiz2 = (-b - delta ** 0.5) / (2*a)
        return raiz1, raiz2
      
      elif delta == 0:
        raiz = -b / (2*a)
        return raiz
      
      else:
        return 'Não há raizes existentes'


def plot_quadratica(a, b, c):
    x  = np.linspace(-10, 10, 50)
    y = funcao_quadratica(x, a, b, c)
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.title('Gráfico de uma Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()



def fatorial(a):
    fat = 1
    for i in range(1, a+1):
        fat *= i
    return fat
            
def plot_fatorial(n):
    x = list(range(n + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x , y , marker= 'o', linestyle= '-')
    plt.title('Grafico Fatorial')
    plt.xlabel('Numero')
    plt.ylabel('Fatorial')
    plt.grid(True)
    plt.show()
 
    result = int(input('Insira o numero para o fatorial: '))
    print(plot_fatorial(result))

def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    num1 = int(input('Digite o primeiro numero: '))
                    num2 = int(input('Digite o segundo numero: '))
                    print(f'O Resultado da soma de {num1} + {num2} é {soma(num1,num2)}')
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    num1 = int(input('Digite o primeiro numero: '))
                    num2 = int(input('Digite o segundo numero: '))
                    print(f'O Resultado da subtração de {num1} - {num2} é ')
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    num1 = int(input('Digite o primeiro numero: '))
                    num2 = int(input('Digite o segundo numero: '))
                    print(f'O Resultado da multiplicação de {num1} X {num2} é {multiplicacao(num1,num2)}  ')
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    num1 = int(input('Digite o primeiro numero: '))
                    num2 = int(input('Digite o segundo numero: '))
                    print(f' O Resultado da divisão {num1} / {num2} é {divisao(num1,num2)} ')
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    num1 = int(input('Digite o valor de a: '))
                    num2 = int(input('Digite o valor do expoente: '))
                    print(f' O valor da função exponencial f({num1}) é {exponencial(num1,num2)} {plot_exponencial(num1,num2)} ')
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    num1 = int(input('Digite o valor de a: '))
                    num2 = int(input('Digite o valor de b: '))
                    num3 = int(input('Digite o valor de c: '))
                    print(f'As raizes da sua função quadratica são: {calcular_raizes(num1,num2,num3)}')
                    print(plot_quadratica(num1,num2,num3))
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    a = int(input('Digite o valor de a: '))
                    x = int(input('Digite o valor de x: '))
                    b = int(input('Digite o valor de b: '))
                    print(f'O resulado de sua função é: {linear(x,a,b)}')
                    print(plot_linear(x,a,b))
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL X!)")
                    num1 = int(input('Digite o valor para o fatorial: '))
                    print(f'O resultado do fatorial é: {fatorial(num1)}')
                    print(plot_fatorial(num1))
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()