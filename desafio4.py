lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

# O programa deve solicitar a sigla da uf e excluir as informações
# caso a sigla informada exista na lista, lembrar de excluir das 
# demais listas.
entrada = str.upper(input('informe a UF: '))
posicao_uf_sigla = lst_siglas['RN']

del lst_siglas[posicao_uf_sigla]
del lst_populacao[posicao_uf_sigla]
del lst_siglas[posicao_uf_sigla]

print(f'{lst_siglas}')
print(f'{lst_populacao}')
print(f'{lst_siglas}')