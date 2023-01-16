from rich import print
import os


votos_bolsonaro = 0
votos_lula = 0


while True:
    #Candidatos
    print("=" * 20)
    print(f"[on green]TOTAL BOLSONARO:[/] {votos_bolsonaro}{os.linesep}[on red]TOTAL LULA:[/] {votos_lula}")
    print("=" * 20)
    #Votos
    try:
        voto = int(input(f"Pra quem gostaria de votar?{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}seu voto: "))

        if voto == 1:
            votos_bolsonaro += 1
        elif voto == 2:
            votos_lula += 1
        else:
            pass
    except:
        print("Digite apenas 1 ou 2")
    os.system("clear")