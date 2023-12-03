#Integrando el codigo

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sympy import sympify,latex

from principal import principal


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Convertidor de Fórmulas a LaTeX")

        # Etiqueta y campo de entrada
        self.etiqueta = tk.Label(ventana, text="Ingrese la fórmula:")
        self.etiqueta.pack()

        self.entrada_formula = tk.Entry(ventana, width=40)
        self.entrada_formula.pack()

        # Etiqueta y campo de entrada
        self.etiqueta = tk.Label(ventana, text="Ingrese los intervalos separados por una coma:")
        self.etiqueta.pack()

        self.entrada_Intervalor = tk.Entry(ventana, width=40)
        self.entrada_Intervalor.pack()

        # Botón para convertir a LaTeX y mostrar visualmente
        self.boton_convertir = tk.Button(ventana, text="Mostrar formula", command=self.convertir_y_mostrar)
        self.boton_convertir.pack()

        # Botón para Graficar y derivar
        self.boton_convertir = tk.Button(ventana, text="Derivar", command=self.main) #Cambiar funcion por llamar al metodo main del otro archivo python
        self.boton_convertir.pack()



        # Etiqueta para mostrar la fórmula LaTeX
        self.etiqueta_formula = tk.Label(ventana, text="")
        self.etiqueta_formula.pack()

        # Canvas para renderizar un dibujo
        self.figura, self.ax = plt.subplots(figsize=(4, 3))
        self.ax.axis("off")  # Desactivar ejes
        self.figura_canvas = FigureCanvasTkAgg(self.figura, master=ventana)
        self.figura_canvas_widget = self.figura_canvas.get_tk_widget()
        self.figura_canvas_widget.pack()

    def convertir_y_mostrar(self):
        # Obtener la fórmula desde la entrada
        formula_texto = self.entrada_formula.get()

        print(formula_texto)
        print(sympify(formula_texto))
        print(latex(sympify(formula_texto)))
        #Convertir String a Formato valido para latex
        funcionLatex = (latex(sympify(formula_texto)))


        # Agregar leyenda y etiquetas
        self.ax.plot([1], [1], label=f'Función : ${funcionLatex}$')
        self.ax.legend()
        self.ax.set_title('Su Función')
        self.ax.set_xlabel('Eje X')
        self.ax.set_ylabel('Eje Y')

        # Actualizar el lienzo
        self.figura_canvas.draw()
    def main(self):
        principal(self)
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = Aplicacion(ventana_principal)
    ventana_principal.mainloop()
