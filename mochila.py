nomes = []
pesos = []

total = 0

while True:
 nome = input("\nDigite o nome do objeto que vc vai levar na sua mochila \n ou digite FIM se nao possui mais nada para adicionar a mochila:\n " )

 if nome.upper() == "FIM" : 
    break

 while True:
    try:
         kg = input("\nDigite o peso do item em kg: ")

         peso = float(kg)

    except:
      peso = float(kg.replace(",", "."))

    if peso <= 0:
       print ("\nPor favor, digite um peso válido.")
    else:  
      break
     
nomes.append(nome)
pesos.append(peso)

total += peso

if total > 15:
    print("\nOPAAAA, calma lá patrão!! tem muito peso na mochila, pra não ter dor nas costas, o peso permitido é de 15kg")


print("\n-----MOCHILA DA DORA AVENTUREIRA-----\n")
print("\nMochila, mochila, yeah!!!!")

if len(nomes) == 0:
    print("\nA mochila está vazia, não há itens para mostrar.")
else:
  for sequencia in range(len(nomes)):
    print(f"\nItem:{sequencia + 1}{nomes[sequencia]} - Peso: {pesos[sequencia]} kg")

quantidade_itens = len(nomes)
media_peso = total / quantidade_itens

maior_peso = max(pesos)
posicao_maior_peso = pesos.index(maior_peso)
item_maior_peso = nomes[posicao_maior_peso]

print(f"\n A mochila tem {quantidade_itens} de itens")
print(f"\n O peso total da mochila é de {total:.2f} kg")
print(f"\n A média de peso dos itens é de {media_peso:.2f} kg")
print(f"\n O item com maior peso é {item_maior_peso} com {maior_peso:.2f} kg")

if total > 15:
   excesso = total - 15
   print(f"\n sua mochila ta muito pesada patrao, vc ta carregando {excesso:.2f} kg a mais do que o permitido, tire algo da mochila")

else:
   sobra = 15 - total
   print(f"\n sua mochila ainda tem espaço, vc pode colocar mais {sobra:.2f} kg de peso na mochila")   