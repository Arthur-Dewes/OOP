def valid_cpf(cpf: str) -> bool:
    """Verifica se determinado cpf é valido ou não"""
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False 
    
    digit1, digit2 = 0, 0

    weight = 1
    for i in range(0, 9):
        digit1 += int(cpf[i]) * weight
        weight += 1

    digit1 = digit1 % 11 if digit1 % 11 < 10 else 0

    weight = 0
    for i in range(0, 10):
        digit2 += int(cpf[i]) * weight
        weight += 1

    digit2 = digit2 % 11 if digit2 % 11 < 10 else 0

    if cpf[9:11] == str(digit1) + str(digit2):
        return True
    else:
        return False
