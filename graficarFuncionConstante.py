import matplotlib.pyplot as plt
import sympy as sp
from sympy import latex

def funcionConstante(funcion, intervalo):
    inicioX = intervalo[0]
    finX = intervalo[1]
    print("Hola desde una funcion Constante")
    funcion = sp.sympify(funcion)
    plt.figure(figsize=(10, 5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y su derivada')
    plt.plot([inicioX, finX], [funcion, funcion], color='blue', label=f'Función original: ${latex(funcion)}$')
    plt.plot([inicioX, finX], [0, 0], color='red', label="Derivada: 0")
    plt.scatter([], [], color='blue', marker='o', label=f'No tiene Puntos criticos ni extremos')
    plt.legend()
    plt.grid(True)
    plt.show()

