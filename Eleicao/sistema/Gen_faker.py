from faker import Faker
from faker.providers import BaseProvider, DynamicProvider
import pandas as pd
import random
import numpy as np


f = Faker(['pt_BR'])

#eleitores: 
# pessoas: nome, idade, cpf
# candidatos: nome, num_voto, proposta
# partidos: nome, num, cnpj
#arq urnas: cpf, depFe, depEs, sena, gove, pres

propostas_provider = DynamicProvider(provider_name='escolhe_propostas',
    elements=["Educação", "Transporte Público", "Saúde", "Segurança Pública",
    "Meio Ambiente e Sustentabilidade", "Habitação e Urbanismo", "Cultura e Lazer", "Economia e Emprego"])

f.add_provider(propostas_provider)

pessoas = {'Nome': np.array([f.name() for _ in range(500)]),
        'Idade': np.array([f.random_int(min=18, max=70) for _ in range(500)]),
        'Cpf': np.array([f.cpf() for _ in range(500)])}

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

candidatos = {'Nome': np.array([f.name() for _ in range(209)]),
                'Num_voto': np.array(num_voto),
                'Propostas': np.array([f.escolhe_propostas() for _ in range(209)])}

partidos = {'Nome': np.array(["Avante", "Cidadania", "Democracia Cristã", "Movimento Democrático Brasileiro",
            "Partido Novo", "Patriota", "Partido Comunista Brasileiro", "Partido Comunista do Brasil", 
            "Partido Democrático Trabalhista", "Partido Liberal", "Partido da Mulher Brasileira", 
            "Partido da Mobilização Nacional", "Podemos", "Progressistas", "Partido Pátria Livre", 
            "Partido Republicano da Ordem Social", "Partido Socialista Brasileiro", "Partido Social Cristão",
            "Partido Social Democrático", "Partido da Social Democracia Brasileira", "Partido Social Liberal",
            "Partido Socialismo e Liberdade", "Partido Socialista dos Trabalhadores Unificado",
            "Partido dos Trabalhadores", "Partido Trabalhista Brasileiro", "Partido Trabalhista Cristão",
            "Partido Verde", "Rede Sustentabilidade", "Republicanos", "Solidariedade", "Unidade Popular",
            "União Brasil"]),
            'Num_eleitoral': np.array([70, 23, 27, 15, 30, 51, 21, 65, 12, 22, 44, 33, 19, 11, 18, 22, 40, 20, 55, 45,
                                17, 50, 16, 13, 14, 36, 43, 18, 10, 77, 80, 44]),
            'Cnpj': [f.cnpj() for _ in range(32)]}

df1 = pd.DataFrame(pessoas)
df2 = pd.DataFrame(candidatos)
df3 = pd.DataFrame(partidos)

with open('Eleicao/IO/eleitores.txt', 'x') as file:
    file.write('Pessoas: \n')
    file.write(df1.to_string(header=True, index=False))
    file.write('\nCandidatos: \n')
    file.write(df2.to_string(header=True, index=False))
    file.write('\nPartidos: \n')
    file.write(df3.to_string(header=True, index=False))

with open('Eleicao/IO/urna1.txt', 'x') as file:
    file.write('Urna 1: \n')
    reorg = random.shuffle(df1['Cpf'])
    file.write({'Cpf': reorg, 'depEs': np.array([random.choice(df)]), 'depEs':, 'sena':, 'gove':, 'pres':})