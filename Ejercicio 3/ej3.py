import re

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def encontrar_secuencia_numeros_letras(texto):
    patron = r'\d+[a-zA-Z]+'
    resultados = re.findall(patron, texto)
    return resultados

def encontrar_vocales_repetidas(texto):
    patron = r'\b\w*([aeiouAEIOU])\1{2,}\w*\b'
    resultados = re.findall(patron, texto)
    return resultados

def encontrar_caracteres_especiales(texto):
    patron = r'[^a-zA-Z0-9\s]'
    resultados = re.findall(patron, texto)
    return resultados

def main():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    try:
        contenido = leer_archivo(nombre_archivo)
        secuencia_numeros_letras = encontrar_secuencia_numeros_letras(contenido)
        vocales_repetidas = encontrar_vocales_repetidas(contenido)
        caracteres_especiales = encontrar_caracteres_especiales(contenido)
        
        print("Secuencia de números seguidos de letras encontrada:")
        print(secuencia_numeros_letras if secuencia_numeros_letras else "No se encontraron coincidencias")
        
        print("\nPalabras con más de tres vocales iguales encontradas:")
        print(vocales_repetidas if vocales_repetidas else "No se encontraron coincidencias")
        
        print("\nCaracteres especiales encontrados:")
        print(caracteres_especiales if caracteres_especiales else "No se encontraron coincidencias")
        
    except FileNotFoundError:
        print("El archivo no se encontró.")

if __name__ == "__main__":
    main()
