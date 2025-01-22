from sistema import *
import sys

def main(qtd: int):

    if len(sys.argv) < 3:
        raise MissingArgumentError("Há argumentos faltando")
    
    gen_files('Eleicao/IO', qtd) # Gera os arquivos de entrada no diretorio escolhido
    
    arg_eleitores = sys.argv[1]
    arg_urnas = sys.argv[2:]

    pessoas = Eleicao(qtd).read_pessoas(arg_eleitores)
    candidatos = Eleicao(qtd).read_candidatos(arg_eleitores)
    partidos = Eleicao(qtd).read_partidos(arg_eleitores)

    classe_pessoas = [Pessoa(pessoa[0], pessoa[1], pessoa[2]) for pessoa in pessoas]

    # verificar se o nome do candidato está em classe_pessoas
    classe_candidatos = []
    for i in range(len(classe_pessoas)):
        if candidatos[i][0] in [pessoa.get_name() for pessoa in classe_pessoas]:
            # classe_candidato = Candidato(nome, idade, cpf, numero, partido)
            pass


def int_input():
    while True:
        tupni = input("Digite a quantidade de eleitores: ")
        if tupni.isdigit():
            return int(tupni)
        else:
            print("Digite um valor válido")
            continue

if __name__ == '__main__':
    total = int_input()
    main(total)
