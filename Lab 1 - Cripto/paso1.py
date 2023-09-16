import sys

def cifrar_cesar(texto, corrimiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter)
            codigo_cifrado = ((codigo - ord('a') + corrimiento) % 26) + ord('a')
            if mayuscula:
                resultado += chr(codigo_cifrado).upper()
            else:
                resultado += chr(codigo_cifrado)
        else:
            resultado += caracter
    return resultado

if len(sys.argv) != 3:
    print("Uso: python3 cesar.py <texto> <corrimiento>")
    sys.exit(1)

texto_original = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_original, corrimiento)
print(texto_cifrado)
