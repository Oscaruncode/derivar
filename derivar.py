import sympy as sp
import numpy as np

def derivar(strFuncion,intervalo):

    x = sp.symbols("x")
    try:
        expresion = sp.sympify(strFuncion)
    except sp.SympifyError:
        print("Error al analizar la función. Asegúrate de ingresar una expresión válida.")
        return None, None, None, None, None, None, None, None, None

    #Derivada
    derivada = sp.diff(expresion, x)

    #Puntos Criticos
    puntos_criticos = sp.solve(derivada, x) #Calcular puntos criticos                 #pc [x1,x2]
    puntos_criticosY = [sp.lambdify(x, sp.sympify(strFuncion), 'numpy')(p) for p in puntos_criticos]     #pcY [y1,y2]

    #ValoresY del intervalo cerrado
    valoresY_Intervalo = [sp.lambdify(x, sp.sympify(strFuncion), 'numpy')(p) for p in intervalo]

    #Convertir expresion para evaluar
    f = sp.lambdify(x, expresion, 'numpy')
    df = sp.lambdify(x, derivada, 'numpy')

    # Crear datos para la gráfica
    x_vals = np.linspace(-10, 10, 400)           #[-10,-9.9,-]         [x1,x2,x3]
    y_vals = f(x_vals)                                     #f(x) = funcion        [y1,y2,y3]
    dy_vals = df(x_vals)                                   #f'(x)= funcDerivada     [dy1,dy2,dy3]

    return strFuncion, derivada, x_vals, y_vals, dy_vals, intervalo, puntos_criticos, puntos_criticosY, valoresY_Intervalo
