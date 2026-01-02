#Imports
import sys
import string

#Variáveis

alfabeto = list(string.ascii_lowercase)

#Funções
def menu():
    sel = int(input("Menu Principal \n 1-Codificar\n 2-Decodificar\n 3-Sair\n\nSelecione uma opção abaixo: "))
    return sel

def quebrar():
    frase = str(input("Digite a frase a ser codificada: "))
    frase_br = list(frase)
    tam = int(len(frase_br))
    return(frase_br, tam)

def codificar(frase, tam):
    frase_cod = list()
    chave = int(input("Digite a chave a ser utilizada para codificação: "))
    for i in range(tam):
        a = int(alfabeto.index(frase[i]))
        b = ((a + chave) % 26)
        frase_cod.append(alfabeto[b])
        frase_final = "".join(frase_cod)
    return (f"\nA frase foi codificada como {frase_final}")

#Código
print("Bem vindo à Cifra de César!\n")

while(True):

    sel = menu()

    if sel == 1:
        print("\nVocê escolheu codificar")
        frase_br, tam = quebrar()
        print(codificar(frase_br, tam))
        break
    elif sel == 2:
        print ("Você escolheu decodificar")
    elif sel == 3:
        print ("Você escolheu sair.")
        sys.exit(0)
    else :
        print("Nenhuma opção selecionada, selecione a opção correta")