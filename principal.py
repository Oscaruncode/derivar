from GraficarFuncionLineal import GrafFuncionLineal
from extremos_absolutos import extremos_absolutos
from graficarFuncionConstante import funcionConstante
from graficarFuncionVertical import funcionVertical
from graficar_funciones import graficar_funciones
from derivar import derivar
import re
import time

def principal(parametros):
    expresion_str = parametros.entrada_formula.get()
    intervalo_str = parametros.entrada_Intervalor.get()
    print(expresion_str,intervalo_str)
    isVerticalDerivate = False
    try:
        if(re.search("x=", expresion_str)):
            isVerticalDerivate=True
    except:
        print("Continue")
    try:
        intervalo = [float(val) for val in intervalo_str.split(",")]  # Convertir a números reales
    except:
        intervalo = None

    if intervalo is None:
        print("El intervalo ingresado es invalido")
    elif isVerticalDerivate:   #Agregar funcion derivada de x=valor
        funcionVertical(expresion_str,intervalo)
        time.sleep(5)
        quit()
        #graficar_funciones(expresion_str, derivada, x_vals, y_vals, dy_vals, intervalo, puntosCriticos, puntosCriticosY, valoresY_Intervalo, extremos) #Graficar funcion con derivada indeterminada, de la forma x=2
    else:
        strFuncion, derivada, x_vals, y_vals, dy_vals, intervalo, puntosCriticos, puntosCriticosY, valoresY_Intervalo = derivar(expresion_str, intervalo)

    if intervalo is None:
        print("El intervalo ingresado es invalido o la funcion ingresada es invalida")
    elif strFuncion is None:  #Verifica si la expresion es valida
        print("INGRESE UNA FUNCION VALIDA")
    elif derivada.is_zero:  #Verifica si es una funcion de una constante
        print("Funcion Constante")
        funcionConstante(expresion_str, intervalo)
        time.sleep(5)
        quit()
    elif derivada.is_constant(): #verifica si es una funcion lineal
        GrafFuncionLineal(strFuncion,derivada, intervalo)
    else:
        extremos = extremos_absolutos(intervalo,valoresY_Intervalo,puntosCriticos,puntosCriticosY)  #devuelve [ [minX,maxX] , [minY,maxY   ]
        graficar_funciones(strFuncion, derivada, x_vals, y_vals, dy_vals, intervalo, puntosCriticos, puntosCriticosY, valoresY_Intervalo, extremos)