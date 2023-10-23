import re

# Función para capitalizar la primera letra y agregar un '0' al final
def modify_password(password):
    return password[0].upper() + password[1:] + '0'

# Nombre del archivo de entrada
input_file = 'rockyou.txt'

# Leer el archivo de entrada con la codificación ISO-8859-1
with open(input_file, 'r', encoding='iso-8859-1') as file:
    lines = file.readlines()

# Filtrar y modificar las contraseñas
modified_passwords = []
for line in lines:
    password = line.strip()
    if re.match(r'^[a-zA-Z]', password) and not re.match(r'^\d', password):
        modified_passwords.append(modify_password(password))

# Contar la cantidad de contraseñas modificadas
count_modified_passwords = len(modified_passwords)

# Nombre del archivo de salida
output_file = 'rockyou_mod.dic'

# Escribir las contraseñas modificadas en el nuevo archivo
with open(output_file, 'w') as file:
    file.write('\n'.join(modified_passwords))

print(f'Se han modificado y guardado {count_modified_passwords} contraseñas en {output_file}')

