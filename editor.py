def altera_atividade(pessoas, nova_atividade):
    for pessoa in pessoas:
        pessoa['atividade'] = nova_atividade
    return pessoas
