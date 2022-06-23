
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'python'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    
    enforcou = False
    acertou = False

    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input('Qual letra?')
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        print(letras_acertadas)
        
    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()
