# from matplotlib import pyplot
from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import R, S, trapezoid, triangular
from matplotlib import pyplot


def main():
    pyplot.rc("figure", figsize=(4, 4))

    idade = Domain("idade", 0, 100, res=1)
    imc = Domain("imc", 0, 50, res=0.1)
    glicose = Domain("glicose", 0, 200, res=0.1)
    atividade = Domain("atividade", 0, 10, res=0.1)

    risco = Domain("risco_diabetes", 0, 100, res=0.1)

    idade.jovem = S(20, 45)
    idade.adulto = triangular(18, 50)
    idade.idoso = R(20, 45)

    # idade.jovem.plot()
    # idade.adulto.plot()
    # idade.idoso.plot()

    # pyplot.show()

    imc.baixo = S(18, 22)
    imc.normal = trapezoid(18, 21, 24, 27)
    imc.sobrepeso = trapezoid(21, 25, 28, 29.9)
    imc.obesidade = R(25, 30)

    # imc.baixo.plot()
    # imc.normal.plot()
    # imc.sobrepeso.plot()
    # imc.obesidade.plot()

    # pyplot.show()

    glicose.baixa = S(60, 85)
    glicose.normal = trapezoid(60, 75, 95, 110)
    glicose.alta = trapezoid(80, 100, 120, 140)
    glicose.muito_alta = R(100, 130)

    # glicose.baixa.plot()
    # glicose.normal.plot()
    # glicose.alta.plot()
    # glicose.muito_alta.plot()

    # pyplot.show()

    atividade.baixa = S(2, 5)
    atividade.media = trapezoid(1, 4, 6, 8)
    atividade.alta = R(5, 8)

    # atividade.baixa.plot()
    # atividade.media.plot()
    # atividade.alta.plot()

    # pyplot.show()

    risco.baixo = S(25, 65)
    risco.medio = trapezoid(20, 40, 65, 80)
    risco.alto = R(40, 80)

    # risco.baixo.plot()
    # risco.medio.plot()
    # risco.alto.plot()

    # pyplot.show()

    qualquer_idade = idade.jovem | idade.adulto | idade.idoso
    qualquer_imc = imc.baixo | imc.normal | imc.sobrepeso | imc.obesidade
    qualquer_atividade = atividade.baixa | atividade.media | atividade.alta
    qualquer_glicose = glicose.baixa | glicose.normal | glicose.alta | glicose.muito_alta

    rules = Rule({
        (qualquer_idade, qualquer_imc, glicose.baixa, qualquer_atividade): risco.baixo,
        (qualquer_idade, qualquer_imc, glicose.normal, qualquer_atividade): risco.baixo,
        (qualquer_idade, qualquer_imc, glicose.alta, qualquer_atividade): risco.medio,
        (qualquer_idade, qualquer_imc, glicose.muito_alta, qualquer_atividade): risco.alto,
        (idade.jovem, qualquer_imc, qualquer_glicose, qualquer_atividade): risco.baixo,
        (idade.adulto, qualquer_imc, qualquer_glicose, qualquer_atividade): risco.medio,
        (idade.idoso, qualquer_imc, qualquer_glicose, qualquer_atividade): risco.alto,
        (qualquer_idade, imc.obesidade, qualquer_glicose, qualquer_atividade): risco.alto,
        (qualquer_idade, imc.sobrepeso, qualquer_glicose, qualquer_atividade): risco.alto,
        (qualquer_idade, qualquer_imc, qualquer_glicose, atividade.baixa): risco.alto,
        (qualquer_idade, qualquer_imc, qualquer_glicose, atividade.media): risco.baixo,
        (qualquer_idade, qualquer_imc, qualquer_glicose, atividade.alta): risco.baixo,
    })

    test = {
        idade: 50,
        imc: 22,
        glicose: 120,
        atividade: 1,
    }

    print(rules(test, method='cog'))


if __name__ == '__main__':

    main()
