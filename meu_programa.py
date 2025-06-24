# meu_programa.py
import random

class EscolhaUsuario:
    def __init__(self, entrada_usuario: int):
        self.entrada = entrada_usuario

    def processar(self):
        if self.entrada == 0:
            return self.gerar_string_random()
        else:
            return "Entrada inválida"

    def gerar_string_random(self):
        opcoes = ["olá", "teste", "python", "mensagem aleatória", "string qualquer"]
        return random.choice(opcoes)


if __name__ == "__main__":
    entrada = int(input("Digite 0 para gerar senha: "))
    obj = EscolhaUsuario(entrada)
    print(obj.processar())
