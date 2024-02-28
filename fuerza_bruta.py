from string import ascii_lowercase
import getpass
import string

clave = getpass.getpass("entre la contraseña solo en letras").lower()

checks = 0

for i, char in enumerate(clave):
    if char == clave:
        print("password correcta")
    elif char != clave:
        i + 1
        checks += 1
print("La contraseña fue forzada en: ", checks)
