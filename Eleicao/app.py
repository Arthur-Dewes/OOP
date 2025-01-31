from sistema import *
import sys

def main():

    if len(sys.argv) < 3:
        raise MissingArgumentError("Há argumentos faltando") # encerra o programa caso não haja argumentos suficientes
    
    arg_eleitores = sys.argv[1]
    arg_urnas = sys.argv[2:]

    def plinha(filepath: str) -> int | FileError:
        """Retorna a quantidade de pessoas no arquivo eleitores.txt"""
        count = 0
        with open(filepath, 'r') as file:
            for linha in file:
                if 'candidatos' in linha.lower():
                    return count - 1 # menos a linha de cabeçalho
                count += 1  
        raise FileError(filepath) # encerra o programa caso o arquivo não esteja na formatação correta
    
    qtd = plinha(arg_eleitores)
    pessoas = Eleicao(qtd).read_pessoas(arg_eleitores)
    candidatos = Eleicao(qtd).read_candidatos(arg_eleitores)
    partidos = Eleicao(qtd).read_partidos(arg_eleitores)

    classe_pessoas = []
    for pessoa in pessoas:
        try:
            if type(pessoa[0]) != str or len(pessoa[0]) <= 1:
                raise NotPythonNameError(pessoa[0])
            if not (18 <= int(pessoa[1]) <= 120):
                raise AgeError(pessoa[1])
            if type(pessoa[2]) != str or (len(pessoa[2]) != 14 and pessoa[2].isdigit()) or (len(pessoa[2]) != 11 and not pessoa[2].isdigit()):
                raise CpfError(pessoa[2])

            classe_pessoas.append(Pessoa(pessoa[0], int(pessoa[1]), pessoa[2]))
        except ValueError as e:
            with open("Eleicao/IO/log.txt", "a") as log_file:
                log_file.write(f"Erro ao converter votos: {e}\n")
        except (NotPythonNameError, AgeError, CpfError):
            pass
        except Exception as e:
            with open("Eleicao/IO/log.txt", "a") as log_file:
                log_file.write(f"Erro inesperado -> classe_pessoa: {e}\n")

    def get_cargo(filepath: str, qtd: int) -> tuple:
        """Retorna uma tupla com as pessoas por cargo no padrao: depFe, depEs, sena, gove, pres"""
        with open(filepath, "r") as file:
            linhas = file.readlines()[qtd + 1:qtd + 2 + 209]
            linhas = ([info.strip().split(',')[0] for info in linhas[1:70]], [info.strip().split(',')[0] for info in linhas[70:164]],
                    [info.strip().split(',')[0] for info in linhas[164:184]], [info.strip().split(',')[0] for info in linhas[184:194]], 
                    [info.strip().split(',')[0] for info in linhas[194:]])
            return linhas

    aux_dict = {pessoa.name: pessoa for pessoa in classe_pessoas}
    classe_candidatos = []
    pessoa_por_cargo = get_cargo(arg_eleitores, qtd)
    
    for candidato in candidatos:
        try:
            if int(candidato[1]) <= 10 or int(candidato[1]) >= 99999: # colocar um erro de num_voto == WASD valores para erropra dar erro ao converter
                raise NotPythonValueError(candidato[1])
            if not isinstance(candidato[2], str) or len(candidato[2]) == 0: # colocar erro de proposta
                raise ProposalError(candidato[2])
            
            if candidato[0] in aux_dict.keys() and candidato[0] in pessoa_por_cargo[0]: # erro no abc de candidatos
                classe_candidatos.append(DepFederal(candidato[0], int(aux_dict[candidato[0]].idade), aux_dict[candidato[0]].cpf,  int(candidato[1]), candidato[2]))
            elif candidato[0] in aux_dict.keys() and candidato[0] in pessoa_por_cargo[1]:
                classe_candidatos.append(DepEstadual(candidato[0], int(aux_dict[candidato[0]].idade), aux_dict[candidato[0]].cpf,  int(candidato[1]), candidato[2]))
            elif candidato[0] in aux_dict.keys() and candidato[0] in pessoa_por_cargo[2]:
                classe_candidatos.append(Senador(candidato[0], int(aux_dict[candidato[0]].idade), aux_dict[candidato[0]].cpf,  int(candidato[1]), candidato[2]))
            elif candidato[0] in aux_dict.keys() and candidato[0] in pessoa_por_cargo[3]:
                classe_candidatos.append(Governador(candidato[0], int(aux_dict[candidato[0]].idade), aux_dict[candidato[0]].cpf,  int(candidato[1]), candidato[2]))
            elif candidato[0] in aux_dict.keys() and candidato[0] in pessoa_por_cargo[4]:
                classe_candidatos.append(Presidente(candidato[0], int(aux_dict[candidato[0]].idade), aux_dict[candidato[0]].cpf,  int(candidato[1]), candidato[2]))
        except ValueError as e:
            with open("Eleicao/IO/log.txt", "a") as log_file:
                log_file.write(f"Erro ao converter votos: {e}\n")
        except (NotPythonValueError, ProposalError):
            pass
        except Exception as e:
            with open("Eleicao/IO/log.txt", "a") as log_file:
                log_file.write(f"Erro inesperado -> classe_candidatos: {e}\n")

    #fazer classe_partido

if __name__ == '__main__':
    main()
