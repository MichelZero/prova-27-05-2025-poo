#
# 5. (Médio) Análise de Dados com Dicionários:
# Problema: Você tem uma lista de logs de acesso a um site, 
# onde cada log contém o endereço IP do usuário e a página acessada. 
# Crie um dicionário que conte quantas vezes cada IP acessou cada página.
# Exemplo:
logs = [
    {"ip": "192.168.1.1", "pagina": "/home"},
    {"ip": "192.168.1.2", "pagina": "/produtos"},
    {"ip": "192.168.1.1", "pagina": "/produtos"},
    {"ip": "192.168.1.1", "pagina": "/home"},
    {"ip": "192.168.1.2", "pagina": "/contato"},
]

# Saída esperada (aproximada):
# {
#     '192.168.1.1': {'/home': 2, '/produtos': 1},
#     '192.168.1.2': {'/produtos': 1, '/contato': 1}
# }


contagem_acessos = {}
for log in logs:
    ip = log["ip"]
    pagina = log["pagina"]
    if ip not in contagem_acessos:
        contagem_acessos[ip] = {}  # Inicializa o dicionário para o IP
    if pagina in contagem_acessos[ip]:
        contagem_acessos[ip][pagina] += 1
    else:
        contagem_acessos[ip][pagina] = 1




print(contagem_acessos)  # Imprime o dicionário de contagem de acessos