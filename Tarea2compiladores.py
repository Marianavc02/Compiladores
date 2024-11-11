# Función para encontrar una producción en la gramática
def encontrarEnGramatica(prod, gramatica):
    return gramatica.get(prod, "NA")  # Si no se encuentra la producción, devuelve "NA"

# Función para generar todas las posibles divisiones de una cadena en dos subcadenas
def generarSubstrings(primer_idx, length):
    sub_strings = []
    for i in range(1, length):  # Itera sobre las posibles posiciones de corte
        primera = (primer_idx, primer_idx + i)  # Primera subcadena
        segunda = (primer_idx + i, primer_idx + length)  # Segunda subcadena
        par = (primera, segunda)  # Par de índices que representan las subcadenas
        sub_strings.append(par)  # Agrega el par a la lista
    return sub_strings

# Implementación del algoritmo CYK para analizar una cadena con una gramática libre de contexto
def cky(input_string, gramatica):
    n = len(input_string) + 1  # Longitud de la cadena más 1
    Tabla = [["" for _ in range(n)] for _ in range(n)]  # Tabla para almacenar las producciones

    # Recorre todos los posibles tamaños de subcadenas
    for length in range(1, n):
        resta = n - length  # Calcula cuántas subcadenas de esa longitud hay
        for i in range(resta):  # Itera sobre las posiciones iniciales de las subcadenas
            val = ""
            if length > 1:
                # Genera todas las posibles divisiones de la subcadena
                sub_strings = generarSubstrings(i, length)
                for sub_str in sub_strings:
                    # Obtiene los índices de las subcadenas
                    x1, y1 = sub_str[0]
                    x2, y2 = sub_str[1]
                    # Concatena los valores de las subcadenas para formar una nueva producción
                    prod = Tabla[x1][y1] + Tabla[x2][y2]
                    # Busca la producción en la gramática
                    val = encontrarEnGramatica(prod, gramatica)
                    if val != "NA":  # Si encuentra una producción válida, detiene la búsqueda
                        break
            else:
                # Si la longitud es 1, simplemente busca el símbolo terminal en la gramática
                val = encontrarEnGramatica(input_string[i], gramatica)
            # Almacena el valor encontrado en la tabla
            Tabla[i][i + length] = val

    # Verifica si el símbolo inicial "S" se puede generar a partir de toda la cadena
    return Tabla[0][n - 1] == "S"

# Función principal que maneja la entrada y salida
def main():
    casos = int(input())  # Número de casos de prueba
    output = []
    
    for _ in range(casos):
        lines, strings = map(int,input().split())# Número de líneas de gramática,cadenas a analizar
        gramatica = {}  # Diccionario para almacenar la gramática
        
        # Lee las producciones de la gramática
        for _ in range(lines):
            produccion = input().strip()  # Línea de producción
            head = produccion[0]  # Parte izquierda de la producción
            derivar = ""
            
            if len(produccion) == 3:  # Si es una producción simple (A -> a)
                derivar = produccion[2]
                gramatica[derivar] = head  # Almacena la producción en el diccionario
            else:  # Si la producción tiene múltiples derivaciones
                i = 2
                while i < len(produccion):
                    if produccion[i] == ' ':  # Ignora los espacios
                        i += 1
                        continue
                    if i + 1 < len(produccion) and produccion[i + 1] != ' ':  # Si es una derivación doble (A -> BC)
                        derivar = produccion[i:i + 2]
                        i += 2
                    else:  # Derivación simple (A -> a)
                        derivar = produccion[i]
                        i += 1
                    gramatica[derivar] = head  # Almacena la producción en el diccionario
        
        # Analiza cada cadena con el algoritmo CYK
        for _ in range(strings):
            x = input().strip()  # Cadena a analizar
            if cky(x, gramatica):  # Si la cadena pertenece al lenguaje generado por la gramática
                output.append("yes")
            else:  # Si la cadena no pertenece al lenguaje
                output.append("no")
    
    print("\n".join(output))  # Imprime los resultados

# Llama a la función principal
if __name__ == "__main__":
    main()

