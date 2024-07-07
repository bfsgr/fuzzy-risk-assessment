from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import R, S, trapezoid, triangular
from matplotlib import pyplot

class raciocionador():
    def __init__(self):
        pyplot.rc("figure", figsize=(4, 4))

        self.idade = Domain("idade", 0, 100, res=1)
        self.imc = Domain("imc", 0, 50, res=0.1)
        self.glicose = Domain("glicose", 0, 200, res=0.1)
        self.atividade = Domain("atividade", 0, 10, res=0.1)

        self.risco = Domain("risco_diabetes", 0, 100, res=0.1)

        self.idade.jovem = S(20, 45)
        self.idade.adulto = triangular(18, 50)
        self.idade.idoso = R(20, 45)

        # idade.jovem.plot()
        # idade.adulto.plot()
        # idade.idoso.plot()

        # pyplot.show()

        self.imc.baixo = S(18, 22)
        self.imc.normal = trapezoid(18, 21, 24, 27)
        self.imc.sobrepeso = trapezoid(21, 25, 28, 29.9)
        self.imc.obesidade = R(25, 30)

        # imc.baixo.plot()
        # imc.normal.plot()
        # imc.sobrepeso.plot()
        # imc.obesidade.plot()

        # pyplot.show()

        self.glicose.baixa = S(60, 85)
        self.glicose.normal = trapezoid(60, 75, 95, 110)
        self.glicose.alta = trapezoid(80, 100, 120, 140)
        self.glicose.muito_alta = R(100, 130)

        # glicose.baixa.plot()
        # glicose.normal.plot()
        # glicose.alta.plot()
        # glicose.muito_alta.plot()

        # pyplot.show()

        self.atividade.baixa = S(2, 5)
        self.atividade.media = trapezoid(1, 4, 6, 8)
        self.atividade.alta = R(5, 8)

        # atividade.baixa.plot()
        # atividade.media.plot()
        # atividade.alta.plot()

        # pyplot.show()

        self.risco.baixo = S(25, 65)
        self.risco.medio = trapezoid(20, 40, 65, 80)
        self.risco.alto = R(40, 80)

        # risco.baixo.plot()
        # risco.medio.plot()
        # risco.alto.plot()

        # pyplot.show()

        self.qualquer_idade = self.idade.jovem | self.idade.adulto | self.idade.idoso
        self.qualquer_imc = self.imc.baixo | self.imc.normal | self.imc.sobrepeso | self.imc.obesidade
        self.qualquer_atividade = self.atividade.baixa | self.atividade.media | self.atividade.alta
        self.qualquer_glicose = self.glicose.baixa | self.glicose.normal | self.glicose.alta | self.glicose.muito_alta

        self.rules = Rule({
            (self.qualquer_idade, self.qualquer_imc, self.glicose.baixa, self.qualquer_atividade): self.risco.baixo,
            (self.qualquer_idade, self.qualquer_imc, self.glicose.normal, self.qualquer_atividade): self.risco.baixo,
            (self.qualquer_idade, self.qualquer_imc, self.glicose.alta, self.qualquer_atividade): self.risco.medio,
            (self.qualquer_idade, self.qualquer_imc, self.glicose.muito_alta, self.qualquer_atividade): self.risco.alto,
            (self.idade.jovem, self.qualquer_imc, self.qualquer_glicose, self.qualquer_atividade): self.risco.baixo,
            (self.idade.adulto, self.qualquer_imc, self.qualquer_glicose, self.qualquer_atividade): self.risco.medio,
            (self.idade.idoso, self.qualquer_imc, self.qualquer_glicose, self.qualquer_atividade): self.risco.alto,
            (self.qualquer_idade, self.imc.obesidade, self.qualquer_glicose, self.qualquer_atividade): self.risco.alto,
            (self.qualquer_idade, self.imc.sobrepeso, self.qualquer_glicose, self.qualquer_atividade): self.risco.alto,
            (self.qualquer_idade, self.qualquer_imc, self.qualquer_glicose, self.atividade.baixa): self.risco.alto,
            (self.qualquer_idade, self.qualquer_imc, self.qualquer_glicose, self.atividade.media): self.risco.baixo,
            (self.qualquer_idade, self.qualquer_imc, self.qualquer_glicose, self.atividade.alta): self.risco.baixo,
        })


    def calcular_unica_instancia(self):
        test = {
            self.idade: 50,
            self.imc: 22,
            self.glicose: 120,
            self.atividade: 1,
        }

        print(self.rules(test, method='cog'))


if __name__ == '__main__':

    experimento = raciocionador()
    experimento.calcular_unica_instancia()
