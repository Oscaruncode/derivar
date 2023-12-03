import matplotlib.pyplot as plt
import sympy as sp
from sympy import latex

def graficar_funciones(strFuncion, derivada, x_vals, y_vals, dy_vals, intervalo, puntosCriticos, puntosCriticosY, valoresY_Intervalo, extremos):
    strFuncion = sp.sympify(strFuncion)
    x = sp.symbols("x")

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label=f'Función original: ${latex(strFuncion)}$')
    plt.plot(x_vals, dy_vals, label=f'Derivada: ${latex(derivada)}$')
    plt.scatter(puntosCriticos, puntosCriticosY,color='yellow', marker='o', label=f'Puntos Críticos:(Valores x y de los pc) {" ".join([f"({x}, {y})" for x, y in zip(puntosCriticos, puntosCriticosY)])}')
    plt.scatter(intervalo, valoresY_Intervalo, color='blue', marker='o', label=f'Extremos del intervalo cerrado:(Valores x y de cada coordenada x del intervalo) {" ".join([f"({x}, {y})" for x, y in zip(intervalo, valoresY_Intervalo)])}')
    plt.scatter(extremos[0], extremos[1], color='red', marker='o', label=f'Extremos (Minimo-Maximo): {" ".join([f"({x}, {y})" for x, y in zip(extremos[0], extremos[1])])}')
    plt.title('Función y su Derivada')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
