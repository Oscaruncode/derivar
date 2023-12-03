def extremos_absolutos(intervalo, valoresY_Intervalo, puntosCriticos, puntosCriticosY):
    print("////////////////")
    print(intervalo, valoresY_Intervalo, puntosCriticos, puntosCriticosY)
    valoresX = intervalo + puntosCriticos
    valoresY = valoresY_Intervalo + puntosCriticosY

    # Encontrar el índice del valor máximo en la lista valoresY
    indice_maximo = valoresY.index(max(valoresY))

    # Encontrar el índice del valor mínimo en la lista valoresY
    indice_minimo = valoresY.index(min(valoresY))

    extremosX = [valoresX[indice_minimo], valoresX[indice_maximo]]
    extremosY = [valoresY[indice_minimo], valoresY[indice_maximo]]
    extremos = [extremosX, extremosY]

    return extremos  # devuelve [ [minX,maxX] , [minY,maxY   ]
