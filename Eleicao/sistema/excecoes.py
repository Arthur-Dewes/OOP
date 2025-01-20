class FileError(Exception):
    def __init__(self, filepath: str):
        self.filepath = filepath
        super().__init__(f"Arquivo não encontrado ou não acessível: {filepath}")
        self.log_error(filepath)

    def log_error(self, filepath: str):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"FileError: Arquivo não encontrado ou não acessível -> {filepath}\n")


class NameError(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Nome inválido: {name}")
        self.log_error(name)

    def log_error(self, name: str):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"NameError: Nome inválido -> {name}\n")

class AgeError(Exception):
    def __init__(self, age: int):
        self.age = age
        super().__init__(f"Idade inválida: {age}")
        self.log_error(age)

    def log_error(self, age: int):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"AgeError: Idade inválida -> {age}\n")

class CpfError(Exception):
    
    @staticmethod
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

        if cpf[9:] == str(digit1) + str(digit2):
            return True
        else:
            return False
    
    def __init__(self, cpf: str):
        self.cpf = (cpf, CpfError.valid_cpf(cpf))
        if not self.cpf[1]:
            self.log_error(cpf)
            super().__init__(f"CPF inválido: {cpf}")

    def log_error(self, cpf: str):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"CpfError: invalid cpf -> {cpf}\n")


class NumberError(Exception):
    def __init__(self, number: int):
        self.number = number
        super().__init__(f"Número inválido: {number}")
        self.log_error(number)

    def log_error(self, number: int):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"NumberError: Número inválido -> {number}\n")

class VoteError(Exception):
    def __init__(self, vote: int):
        self.vote = vote
        super().__init__(f"Voto inválido: {vote}")
        self.log_error(vote)

    def log_error(self, vote: int):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"VoteError: Voto inválido -> {vote}\n")

class ProposalError(Exception):
    def __init__(self, proposal: str):
        self.proposal = proposal
        super().__init__(f"Esta não é uma proposta: {proposal}")
        self.log_error(proposal)

    def log_error(self, proposal: str):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"ProposalError: Proposta inválida -> {proposal}\n")


class CnpjError(Exception):
    
    @staticmethod
    def valid_cnpj(cnpj: str) -> bool:
        """Verifica se determinado cnpj é valido ou não"""
        cnpj = ''.join(filter(str.isdigit, cnpj))

        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False 
        
        digit1, digit2 = 0, 0
        
        weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        aux = 0
        for i in range(0, 12):
            aux += int(cnpj[i]) * weight[i]

        if aux % 11 < 2:
            digit1 = 0
        elif aux % 11 >= 2:
            digit1 = 11 - aux % 11
        
        weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        aux = 0
        for ii in range(0, 13):
            aux += int(cnpj[ii]) * weight[ii]
        
        if aux % 11 < 2:
            digit2 = 0
        elif aux % 11 >= 2:
            digit2 = 11 - aux % 11
        
        if cnpj[12:] == str(digit1) + str(digit2):
            return True
        else:
            return False
    
    def __init__(self, cnpj: str):
        self.cnpj = (cnpj, CnpjError.valid_cnpj(cnpj))
        if not self.cnpj[1]:
            self.log_error(cnpj)
            super().__init__(f"CNPJ inválido: {cnpj}")

    def log_error(self, cnpj: str):
        with open("Eleicao/IO/log.txt", "a") as log_file:
            log_file.write(f"CnpjError: invalid cnpj -> {cnpj}\n")
