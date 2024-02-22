import re

empty = "No se encontraron coincidencias"

def read_file(path):
    with open(path, 'r') as archivo:
        content = archivo.read()
    return content

def find_sequence_of_numbers(text):
    pattern = r'\d+'
    result = re.findall(pattern, text)
    return result if result else empty


def find_sequence_numbers_and_letters(text):
    pattern = r'\d+[a-zA-Z]+'
    result = re.findall(pattern, text)
    return result if result else empty

def find_three_repeated_vowels(text):
    pattern = r'(?i)a{3}|e{3}|i{3}|o{3}|u{3}'
    result = re.findall(pattern, text)
    return result if result else empty

def find_special_character(text):
    pattern = r'[^a-zA-Z0-9\s]'
    result = re.findall(pattern, text)
    return result if result else empty

def main():
    # path = input("Ingrese el nombre del archivo de texto: ")
    path = "test.txt"
   
   
    try:
        content = read_file(path)
     
        result = find_sequence_of_numbers(content)
        print(result if result else empty)

        result = find_sequence_numbers_and_letters(content)
        print(result if result else empty)
      
        result = find_three_repeated_vowels(content)
        print(result if result else empty)

        result = find_special_character(content)
        print(result if result else empty)

        # caracteres_especiales = find_special_character(content)
        
        # print("Secuencia de números seguidos de letras encontrada:")
        # print(secuencia_numeros_letras if secuencia_numeros_letras else "No se encontraron coincidencias")
        
        # print("\nPalabras con más de tres vocales iguales encontradas:")
        # print(vocales_repetidas if vocales_repetidas else "No se encontraron coincidencias")
        
        # print("\nCaracteres especiales encontrados:")
        # print(caracteres_especiales if caracteres_especiales else "No se encontraron coincidencias")
        
    except FileNotFoundError:
        print("El archivo no se encontró.")


