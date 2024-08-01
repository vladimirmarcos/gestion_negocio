def validar_cuit(cuit):
    # Validaciones mínimas
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return False

    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    cuit = cuit.replace("-", "")  # Remuevo las barras

    # Calculo el dígito verificador
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux - (int(aux / 11) * 11))
    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    return aux == int(cuit[10])


print(validar_cuit("20-36586430-"))  # True
