quantidade_turmas = int(input("quantas turmas vão na excursão? "))
while quantidade_turmas <= 0 :
    quantidade_turmas = int(input("deve haver pelo menos uma turma: "))

total_dealunos = 0
maior_turma = ""
mais_inscrito= -1

for i in range(quantidade_turmas):
    turma = input(f"\na {i+1}° tem o nome de : ")
    inscritos = int(input("e quantos incritos ela tem: "))

    while inscritos < 0 :
        inscritos = int(input("a turma precisa ter algum inscrito: "))

    total_dealunos += inscritos

if inscritos > mais_inscrito:
    mais_inscrito = inscritos
    maior_turma = turma

##calculos----

professores = (total_dealunos - 14) // 15
total_participantes = total_dealunos + professores
bus= (total_participantes - 43) // 44
acentos_sobrando = (bus * 44) - total_participantes
custo_bus = bus * 1800
if total_dealunos > 0:
    pago_poraluno = custo_bus / total_dealunos
else:
    pago_poraluno = 0

print("\n /////PLANILHA DA EXCURSAO/////")
print("\nTotal de alunos:", total_dealunos)
print("Professores acompanhantes:", professores)
print("Total de pessoas:", total_participantes)
print("Ônibus necessários:", bus)
print("Lugares que sobram:", acentos_sobrando)
print(f"Custo total: R$ {custo_bus:.2f}")
print(f"Valor por aluno: R$ {pago_poraluno:.2f}")
print("Turma com mais inscritos:", maior_turma)