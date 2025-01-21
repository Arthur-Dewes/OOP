from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import numpy as np
import random

#eleitores: 
## pessoas: nome, idade, cpf
## candidatos: nome, num_voto, proposta
## partidos: nome, num, cnpj
#arq urnas: cpf, depFe, depEs, sena, gove, pres


def gen_files(output_dir: str, num_pessoas: int) -> None:
    def gen_invalid_vote(min_value: int, max_value: int, lista: list):
        while True:
            num_aleatorio = random.randint(min_value, max_value)
            if num_aleatorio not in lista:
                return num_aleatorio

    f = Faker(['pt_BR'])

    propostas_provider = DynamicProvider(provider_name='escolhe_propostas',
        elements=["Educação", "Transporte Público", "Saúde", "Segurança Pública", "Meio Ambiente e Sustentabilidade",
                "Habitação e Urbanismo", "Cultura e Lazer", "Economia e Emprego", "Tecnologia e Inovação",
                "Justiça e Direitos Humanos", "Infraestrutura e Mobilidade Urbana", "Desenvolvimento Rural e Agricultura",
                "Turismo e Patrimônio Cultural", "Ciência e Pesquisa", "Energia e Recursos Naturais", "Inclusão Social e Diversidade"])

    f.add_provider(propostas_provider)

    nomes = np.array([f.name() for _ in range(num_pessoas)])
    pessoas = {'Nome': nomes,
            'Idade': [f.random_int(min=18, max=70) for _ in range(num_pessoas)],
            'Cpf': [f.cpf() for _ in range(num_pessoas)]}

    depFe = [f.unique.random_int(min=1000, max=9999) for _ in range(70)]
    depEs = [f.unique.random_int(min=10000, max=99999) for _ in range(94)]
    sena = [f.unique.random_int(min=100, max=999) for _ in range(20)]
    gove = [f.unique.random_int(min=10, max=99) for _ in range(10)]
    pres = [f.unique.random_int(min=10, max=99) for _ in range(15)]

    num_voto = []
    num_voto.extend(depFe)
    num_voto.extend(depEs)
    num_voto.extend(sena)
    num_voto.extend(gove)
    num_voto.extend(pres)

    candidatos = {'Nome': nomes[[f.unique.random_int(min=0, max=999) for _ in range(209)]],
                    'Num_voto': num_voto,
                    'Propostas': [f.escolhe_propostas() for _ in range(209)]}

    partidos = {'Nome': ["Avante", "Cidadania", "Democracia Cristã", "Movimento Democrático Brasileiro", "Partido Novo", 
                "Patriota", "Partido Comunista Brasileiro", "Partido Comunista do Brasil", "Partido Democrático Trabalhista", 
                "Partido Liberal", "Partido da Mulher Brasileira", "Partido da Mobilização Nacional", "Podemos", "Progressistas",
                "Partido Pátria Livre", "Partido Republicano da Ordem Social", "Partido Socialista Brasileiro", "Partido Social Cristão",
                "Partido Social Democrático", "Partido da Social Democracia Brasileira", "Partido Social Liberal", "Partido Socialismo e Liberdade",
                "Partido Socialista dos Trabalhadores Unificado", "Partido dos Trabalhadores", "Partido Trabalhista Brasileiro", "Partido Trabalhista Cristão",
                "Partido Verde", "Rede Sustentabilidade", "Republicanos", "Solidariedade", "Unidade Popular", "União Brasil"],
                'Num_eleitoral': [70, 23, 27, 15, 30, 51, 21, 65, 12, 22, 44, 33, 19, 11, 18, 22, 40, 20, 55, 45,
                                    17, 50, 16, 13, 14, 36, 43, 18, 10, 77, 80, 44],
                'Cnpj': [f.cnpj() for _ in range(32)]}

    df1 = pd.DataFrame(pessoas)
    df2 = pd.DataFrame(candidatos) 
    df3 = pd.DataFrame(partidos)

    # acrescentando erros ao arquivo
    random_pos_eleitores = np.array([f.unique.random_int(min=2, max=num_pessoas+1) for _ in range(13)])
    random_pos_urnas = [f.unique.random_int(min=0, max=num_pessoas) for _ in range(5)]
    invalid_cpfs = ["123.456.789-00", "111.111.111-11", "000.000.000-00", "222.222.222-22", "333.444.555-66",
                    "999.888.777-00", "555.123.456-78", "444.444.444-00", "123.123.123-11", "678.901.234-56"]

    # - 2 ajusta o índice para o iloc
    random_pos_eleitores = random_pos_eleitores - 2
    
    df1.iloc[random_pos_eleitores[:10], 2] = invalid_cpfs # cpfs inválidos
    df1.iloc[random_pos_eleitores[10], 1] = 17 # menor de idade
    df1.iloc[random_pos_eleitores[11], 0] = "" # nome vazio
    df1.iloc[random_pos_eleitores[12], 2] = "" # cpf vazio

    # voto inválido para cada cargo
    novo_depFe = gen_invalid_vote(1000, 9999, depFe)
    novo_depEs = gen_invalid_vote(10000, 99999, depEs)
    novo_sena = gen_invalid_vote(100, 999, sena)
    novo_gove = gen_invalid_vote(10, 99, gove)
    novo_pres = gen_invalid_vote(10, 99, pres)

    with open(f'{output_dir}/eleitores.txt', 'x') as file:
        file.write('Pessoas: \n')
        for i in range(num_pessoas):
            file.write(f"{df1.iloc[i]['Nome']},{df1.iloc[i]['Idade']},{df1.iloc[i]['Cpf']}\n")
        file.write('Candidatos: \n')
        for i in range(209):
            file.write(f"{df2.iloc[i]['Nome']},{df2.iloc[i]['Num_voto']},{df2.iloc[i]['Propostas']}\n")
        file.write('Partidos: \n')
        for i in range(32):
            file.write(f"{df3.iloc[i]['Nome']},{df3.iloc[i]['Num_eleitoral']},{df3.iloc[i]['Cnpj']}\n")

    num_urnas = num_pessoas // 500
    reorg = df1['Cpf'].tolist()
    random.shuffle(reorg)

    count = 0
    for i in range(num_urnas if num_pessoas % 500 == 0 else num_urnas + 1):
        start_idx = i * 500
        end_idx = min((i + 1) * 500, num_pessoas)

        with open(f'{output_dir}/urna{i + 1}.txt', 'x') as file:
            file.write(f'Urna {i + 1}: \n')
            for _ in range(start_idx, end_idx):
                if count == random_pos_urnas[0] - 2:
                    file.write(f"{reorg[count]},{novo_depFe},{random.choice(df2.iloc[70:164]['Num_voto'].values)},{random.choice(df2.iloc[164:184]['Num_voto'].values)},{random.choice(df2.iloc[184:194]['Num_voto'].values)},{random.choice(df2.iloc[194:]['Num_voto'].values)}\n")
                elif count == random_pos_urnas[1] - 2:
                    file.write(f"{reorg[count]},{random.choice(df2.iloc[:70]['Num_voto'].values)},{novo_depEs},{random.choice(df2.iloc[164:184]['Num_voto'].values)},{random.choice(df2.iloc[184:194]['Num_voto'].values)},{random.choice(df2.iloc[194:]['Num_voto'].values)}\n")
                elif count == random_pos_urnas[2] - 2:
                    file.write(f"{reorg[count]},{random.choice(df2.iloc[:70]['Num_voto'].values)},{random.choice(df2.iloc[70:164]['Num_voto'].values)},{novo_sena},{random.choice(df2.iloc[184:194]['Num_voto'].values)},{random.choice(df2.iloc[194:]['Num_voto'].values)}\n")
                elif count == random_pos_urnas[3] - 2:
                    file.write(f"{reorg[count]},{random.choice(df2.iloc[:70]['Num_voto'].values)},{random.choice(df2.iloc[70:164]['Num_voto'].values)},{random.choice(df2.iloc[164:184]['Num_voto'].values)},{novo_gove},{random.choice(df2.iloc[194:]['Num_voto'].values)}\n")
                elif count == random_pos_urnas[4] - 2:
                    file.write(f"{reorg[count]},{random.choice(df2.iloc[:70]['Num_voto'].values)},{random.choice(df2.iloc[70:164]['Num_voto'].values)},{random.choice(df2.iloc[164:184]['Num_voto'].values)},{random.choice(df2.iloc[184:194]['Num_voto'].values)},{novo_pres}\n")
                else:
                    file.write(f"{reorg[count]},{random.choice(df2.iloc[:70]['Num_voto'].values)},{random.choice(df2.iloc[70:164]['Num_voto'].values)},{random.choice(df2.iloc[164:184]['Num_voto'].values)},{random.choice(df2.iloc[184:194]['Num_voto'].values)},{random.choice(df2.iloc[194:]['Num_voto'].values)}\n")
                count += 1
    return