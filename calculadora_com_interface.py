import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def linear(x, a, b):
    return (a * x) + b

def plot_linear():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        axisx = np.linspace(-10, 10, 100)
        axisy = linear(axisx, a, b)
        plt.plot(axisx, axisy)
        plt.title(f'Gráfico da função linear {a}x + {b}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para a e b.")

def exponencial(a, x):
    return a ** x

def plot_exponencial():
    try:
        a = float(entry_a.get())
        axisx = np.linspace(-10, 10, 100)
        axisy = exponencial(a, axisx)
        plt.plot(axisx, axisy)
        plt.title(f'Gráfico da função exponencial: {a}^x')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para a.")

def funcao_quadratica(x, a, b, c):
    return a * x ** 2 + b * x + c

def plot_quadratica():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        x = np.linspace(-10, 10, 50)
        y = funcao_quadratica(x, a, b, c)
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.title('Gráfico de uma Função Quadrática')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para a, b e c.")

def fatorial(a):
    fat = 1
    for i in range(1, a+1):
        fat *= i
    return fat

def plot_fatorial():
    try:
        n = int(entry_a.get())
        x = list(range(n + 1))
        y = [fatorial(i) for i in x]
        plt.plot(x, y, marker='o', linestyle='-')
        plt.title('Gráfico Fatorial')
        plt.xlabel('Número')
        plt.ylabel('Fatorial')
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor inteiro válido para n.")

def calcular():
    try:
        resultado = eval(display_var.get())
        display_var.set(resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na operação: {e}")

def adicionar_ao_display(valor):
    display_var.set(display_var.get() + str(valor))

def limpar_display():
    display_var.set("")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora")
root.configure(bg="black")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="white", fg="black")
display.grid(row=0, column=0, columnspan=4)

# Botões de números
numeros = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('0', 4, 1)
]

for (texto, linha, coluna) in numeros:
    tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), bg="black", fg= "white",
              command=lambda t=texto: adicionar_ao_display(t)).grid(row=linha, column=coluna)

# Botões de operações
operacoes = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]

for (texto, linha, coluna) in operacoes:
    if texto == '=':
        tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), bg="black", fg="white",
                  command=calcular).grid(row=linha, column=coluna)
    elif texto == 'C':
        tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), bg="black", fg="white",
                  command=limpar_display).grid(row=linha, column=coluna)
    else:
        tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), bg="black", fg="white",
                  command=lambda t=texto: adicionar_ao_display(t)).grid(row=linha, column=coluna)

# Entradas para gráficos
tk.Label(root, text="a:", bg="black", fg="white").grid(row=5, column=0)
entry_a = tk.Entry(root, bg="white", fg="black")
entry_a.grid(row=5, column=1)

tk.Label(root, text="b:", bg="black", fg="white").grid(row=6, column=0)
entry_b = tk.Entry(root, bg="white", fg="black")
entry_b.grid(row=6, column=1)

tk.Label(root, text="c:", bg="black", fg="white").grid(row=7, column=0)
entry_c = tk.Entry(root, bg="white", fg="black")
entry_c.grid(row=7, column=1)

# Botões para gráficos
tk.Button(root, text="Plot Linear", command=plot_linear, bg="black", fg="white").grid(row=5, column=2)
tk.Button(root, text="Plot Exponencial", command=plot_exponencial, bg="black", fg="white").grid(row=6, column=2)
tk.Button(root, text="Plot Quadrática", command=plot_quadratica, bg="black", fg="white").grid(row=7, column=2)
tk.Button(root, text="Plot Fatorial", command=plot_fatorial, bg="black", fg="white").grid(row=8, column=2)

root.mainloop()