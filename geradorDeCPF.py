from random import randint

# Gera um número aleatório de 11 dígitos
numero = str(randint(10000000000, 99999999999))

novoCpf = numero
reverso = 10
total = 0

# Loop que cria o CPF
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novoCpf[index]) * reverso

    # Cria e verifica o dígito
    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        
        total = 0
        novoCpf += str(digito)

print(novoCpf)
