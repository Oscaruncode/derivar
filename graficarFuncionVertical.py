import matplotlib.pyplot as plt
import sympy as sp


def funcionVertical(funcion,intervalo):
    print("Hola desde una funcion vertical")
    partes = funcion.split('=')
    x=partes[1]
   #z es igual a sacar el valor despues del x=
    plt.figure(figsize=(10, 5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y su derivada')
    plt.plot([x,x], [-1000, 1000], color='blue',  label=f'Función original: ${funcion}$')
    plt.plot([], [], label="Derivada: Indeterminada")
    plt.scatter([], [], color='red', marker='o', label=f'No tiene Puntos criticos')

    plt.legend()
    plt.grid(True)
    plt.show()
