import random
import PySimpleGUI as sg

class SimuladroDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo numero (s/n) ?"

        #Layout
        self.layout = [
            [sg.Text("Jogar o dado ?")],
            [sg.Button("sim"),sg.Button("nao")]
        ]

    def Iniciar(self):
        # criar janela
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)

        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        # fazer algo com os valores
        try:
            if self.eventos == "sim" or self.eventos == "s":
                self.GerarValorDoDado()
            elif self.eventos == "nao" or self.eventos == "n":
                print("Agradecemos a sua participação !!")
            else:
                print("Favor digitar sim ou nao")
        except:
            print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladroDeDados()
simulador.Iniciar()
