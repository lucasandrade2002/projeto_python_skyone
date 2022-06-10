
class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def display(self):
        print(f'-> {self.nome} - {self.fone}')


class Squad:
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

    def incluir_techlead(self, techlead):
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)


class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad = squad


class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

    def incluir_dev(self, dev):
        self.devs.append(dev)

    def display(self):
        super().display()
        print(f'Cargo de {self.cargo} na squad {self.squad.nome}\n')


print("\n-=-=-=-=-=-=-=-=-=-=-=Sky.One Solutions=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem-vindo(a) ao sistema de cadastro de Squads!")

while True:
    squads = []
    nome_squad = input("\nNome da Squad: ")
    nome_techlead = input("\nNome do techlead: ")
    fone_techlead = input("\nTelefone do techlead: ")

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    while True:
        nome_dev = input("\nNome do desenvolvedor: ")
        fone_dev = input("\nTelefone do desenvolvedor: ")
        cargo_dev = input("\nCargo do desenvolvedor: ")

        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        option = input("\nDeseja adicionar mais um dev [S/N]: ")
        if option in 'Nn':
            break

    option = input("\nDeseja adicionar mais uma Squad [S/N]: ")
    if option in 'Nn':
        break

for squad in squads:
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\nSquads criadas:")
    print(f'\n------------------------------{squad.nome}------------------------------')
    print(f'TechLead: {squad.techlead.nome}')
    print('\n-----Devs do Squad-----')
    for dev in squad.devs:
        dev.display()
    print(f'-----------------------------{squad.nome}------------------------------')

print("\n-=-=-=-=-=-=-=-=-=-=-=Sky.One Solutions=-=-=-=-=-=-=-=-=-=-=-=")