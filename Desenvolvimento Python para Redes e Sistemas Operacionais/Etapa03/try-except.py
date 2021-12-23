#A sintaxe do try-except é a seguinte:
#try:
# Código que quer tentar executar e verificar erro
#except Exception:
# Código para tratar algum erro
import os


def exemplo():
    while True:
        try:
            x = int(input("Entre com um número: "))

        except ValueError:
            print("Valor inválido. Tente novamente.")
        except Exception:
            print("Houve um problema com o número obtido. Tente novamente.")
        print("10% de", x, "é:", x / 100)
        resposta=input("Você quer finalizar?(S/N)")
        if resposta == 'S'or "s":
            break

def exemplo2():
    try:
        os.mkdir("diretorio_exemplo")
    except FileExistsError:
        print("Arquivo já existente:", "diretorio_exemplo")
    except FileNotFoundError:
        print("O sistema não pode encontrar o caminho especificado:", 'diretorio\\a')
    except:
        print("Erro")





