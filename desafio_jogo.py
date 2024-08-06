class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'usou um ataque desconhecido'
        
        print(f"O {self.tipo} atacou usando {ataque}")

def criar_herois():
    herois = []
    herois.append(Heroi("Arthur", 30, "guerreiro"))
    herois.append(Heroi("Merlin", 150, "mago"))
    herois.append(Heroi("Bruce", 35, "monge"))
    herois.append(Heroi("Ryu", 25, "ninja"))
    return herois

def mostrar_herois(herois):
    print("Heróis disponíveis:")
    for idx, heroi in enumerate(herois):
        print(f"{idx + 1}. {heroi.nome} ({heroi.tipo})")

def selecionar_heroi(herois):
    while True:
        try:
            escolha = int(input("Selecione o herói pelo número (ou 0 para sair): "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(herois):
                return herois[escolha - 1]
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida, por favor insira um número.")

def gerenciar_ataques(herois):
    continuar = True
    while continuar:
        mostrar_herois(herois)
        heroi = selecionar_heroi(herois)
        if heroi:
            heroi.atacar()
        else:
            continuar = False
            print("Ataques encerrados.")
        
        if continuar:
            resposta = input("Deseja continuar os ataques? (s/n): ").lower()
            if resposta != 's':
                continuar = False
                print("Ataques encerrados.")

def main():
    herois = criar_herois()
    gerenciar_ataques(herois)

# Executa o programa
main()

