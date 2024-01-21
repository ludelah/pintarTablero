def colorear_tablero(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            if j < i or j == i:  # Agregar condición para que la primera fila contenga "rojo"
                fila.append('rojo')
            else:
                fila.append('azul')
        tablero.append(fila)
    return tablero

def verificar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(i+1, len(tablero)):
            if tablero[i].count('rojo') == tablero[j].count('rojo'):
                return False
    return True

# Para un tablero de 8x8
tablero_8x8 = colorear_tablero(8)
cumple_condicion = verificar_tablero(tablero_8x8)
print(f"El tablero cumple la condición: {cumple_condicion}")

# Para un tablero de 1000x1000
tablero_1000x1000 = colorear_tablero(1000)
cumple_condicion = verificar_tablero(tablero_1000x1000)
print(f"El tablero cumple la condición: {cumple_condicion}")


#Written by L Delahaye
