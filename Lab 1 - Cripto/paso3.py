import sys
from termcolor import colored

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 decrypt_caesar.py <mensaje_cifrado>")
        sys.exit(1)

    ciphertext = sys.argv[1]

    print("Combinaciones posibles:")

    most_probable_option = None
    highest_score = 0

    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)

        # Evaluar la legibilidad del texto resultante
        # Puedes ajustar este criterio según tus necesidades
        score = sum(1 for char in decrypted_text if char.isalpha() or char.isspace())

        if score > highest_score:
            highest_score = score
            most_probable_option = decrypted_text

        if shift == 9:
            print(colored(f"Corrimiento 9: {decrypted_text}", "green"))
        else:
            print(f"Corrimiento {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
