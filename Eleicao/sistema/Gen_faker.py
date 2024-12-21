from faker import Faker, DynamicProvider

f = Faker(['pt_BR'])

#eleitores: 
# pessoas: nome, idade, cpf
# candidatos: nome, num_voto, proposta
# partidos: nome, num, cnpj
#arq urnas: cpf, depEs, depFe, pres, gove, sena

# for _ in range(500):
#     print(f.name())

# for _ in range(100):
#     print(f.random_int(min=1, max=99)) # pres
#     print(f.random_int(min=1, max=99)) # gove
#     print(f.random_int(min=100, max=999)) # sena
#     print(f.random_int(min=1000, max=9999)) # depFe
#     print(f.random_int(min=10000, max=99999)) # depEs

print(f.cpf())
print(f.cnpj())
print(f.sentence())

propostas_provider = DynamicProvider(provider_name='escolhe_proposas',
    elements=["Educação", "Transporte Público", "Saúde", "Segurança Pública",
    "Meio Ambiente e Sustentabilidade", "Habitação e Urbanismo", "Cultura e Lazer", "Economia e Emprego"])

with open('../IO/Eleitores.txt', 'x') as file:
    pass

