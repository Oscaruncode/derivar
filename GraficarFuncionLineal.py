import matplotlib.pyplot as plt
import sympy as sp
from sympy import latex

def GrafFuncionLineal(funcion,derivada, intervalo):
    x = sp.symbols('x')
    inicioX = intervalo[0]
    finX = intervalo[1]
    funcion = sp.sympify(funcion)

    # Calcula extremos
    y_inicio = funcion.subs(x, inicioX)
    y_fin = funcion.subs(x, finX)

    plt.figure(figsize=(10, 5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y su derivada')
    y1 = funcion.subs(x, inicioX)
    y2 = funcion.subs(x, finX)
    plt.plot([inicioX, finX], [y1, y2], color='blue', label=f'Función original: ${latex(funcion)}$')
    plt.plot([inicioX, finX], [derivada, derivada], color='red', label=f'Derivada: ${latex(derivada)}$')

    plt.scatter( [inicioX,finX],[y_inicio,y_fin] , color='blue', marker='o', label=f'Extremos del intervalo cerrado: $({int(inicioX)}, {int(y_inicio)}) - ({int(finX)}, {int(y_fin)})$')
    plt.scatter([], [], color='red', marker='o', label=f'No tiene Puntos criticos')

    plt.legend()
    plt.grid(True)
    plt.show()