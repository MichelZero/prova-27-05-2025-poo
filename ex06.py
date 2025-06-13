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


contagem_acessos = {} # criando um dicionário vazio para armazenar a contagem de acessos
# Percorre a lista de logs e conta os acessos por IP e página
for log in logs:
    ip = log["ip"] # Obtém o IP do log 
    pagina = log["pagina"] # Obtém a página acessada do log
    # Verifica se o IP já está no dicionário, se não estiver, inicializa com um dicionário vazio
    if ip not in contagem_acessos:
        contagem_acessos[ip] = {}  # Inicializa o dicionário para o IP
    if pagina in contagem_acessos[ip]:
        contagem_acessos[ip][pagina] += 1
    else:
        contagem_acessos[ip][pagina] = 1




print(contagem_acessos)  # Imprime o dicionário de contagem de acessos