from boneco import Boneco
import time
import os

class MyGameHangman():
    def __init__(self) -> None:
        self.error = 0 
        self.cont = 0
        self.exibir_boas_vindas()

    def exibir_boas_vindas(self):
        print("","-="*17, end="-\n")
        time.sleep(0.3)
        print("-=   BEM-VINDO AO GAME DA FORCA!   =-")
        time.sleep(0.3)
        print("-=                                 =-")
        time.sleep(0.3)
        print("-=    Vamos começar a diversão!    =-")
        time.sleep(0.3)
        print("-=    Tente adivinhar a palavra    =-")
        time.sleep(0.3)
        print("-=    antes que o boneco seja      =-")
        time.sleep(0.3)
        print("-=    completamente desenhado.     =-")
        time.sleep(0.3)
        print("-=                                 =-")
        time.sleep(0.3)
        print("-=           GOOD LUCK!            =-")
        print("","-="*17, end="-\n\n")

        os.system("pause")
        os.system("cls")
        self.options()
    
    def options(self):
        print("( 1 ) - PLAY ")
        print("( 2 ) - EXIT \n")

        escolha = input(">> ")
        while True:    
            if escolha == "1":
                os.system("cls")

                print("ESCOLHA A PALAVRA CHAVE: ", end="")
                self.palavra_chave = input("")
                self.palavra_list = self.palavra_chave
                self.palavra_chave_list = ["_"] * len(self.palavra_chave)
                break
                
            if escolha == "2":
                break

        os.system("cls")
        self.starttogame()


    def starttogame(self):

        self.boneco1 = Boneco()
        self.boneco1.exibir_forca(0)
        print(" "*25, " ".join(self.palavra_chave_list))

        print("\n\nDIGITE A LETRA QUE DESEJA: ", end="")
        letra = input("")

        self.verificar(letra)

    def verificar(self, letra):
        if len(letra) == 1:
            letra_encontrada = 0

            for i, j in enumerate(self.palavra_list):
                if letra == j:
                    letra_encontrada = 1
                    self.palavra_chave_list[i] = letra

            if letra_encontrada == 1:
                os.system("cls")
                self.boneco1.exibir_forca(0)
                print(" "*25, " ".join(self.palavra_chave_list))
            else:
                os.system("cls")
                self.error += 1
                self.boneco1.exibir_forca(self.error)
                print(" "*25, " ".join(self.palavra_chave_list))

            if "_" in self.palavra_chave_list:
                self.starttogame()

            elif "_" not in self.palavra_chave_list:
                print("TA ESPERTO EIN, PARABENS A PALAVRA ERÁ: ", "".join(self.palavra_chave_list))

            else:
                os.system("cls")
                print("VOCÊ PERDEU O GAME KKKKK")



MyGameHangman()