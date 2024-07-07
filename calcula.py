import main
import leitor
import editor

def calcula_media_riscos(nome_arquivo):
    pacientes = leitor.leitor_csv(nome_arquivo)

    instancia = main.Raciocinador()

    resultados = [[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(11):
        resultados[i] = []
        editor.altera_atividade(pacientes, i)
        for paciente in pacientes:
            resultados[i].append(instancia.calcular_unica_instancia(paciente))

    riscos = []

    for paciente in range(len(pacientes)):
        soma = 0
        for k in range(11):
            soma = soma + resultados[k][paciente]
        riscos.append(soma/11)

    return pacientes, riscos

def calcula_extremos_riscos(nome_arquivo):
    pacientes = leitor.leitor_csv(nome_arquivo)

    instancia = main.Raciocinador()

    resultados = [[], []]

    editor.altera_atividade(pacientes, 10)
    for paciente in pacientes:
        resultados[0].append(instancia.calcular_unica_instancia(paciente))

    editor.altera_atividade(pacientes, 0)
    for paciente in pacientes:
        resultados[1].append(instancia.calcular_unica_instancia(paciente))

    return pacientes, resultados
