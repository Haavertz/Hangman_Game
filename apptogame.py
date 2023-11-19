from boneco import Boneco
import time
import os

class MyGameHangman():
    def __init__(self) -> None:
        self.error = 0 
        self.palavra_digitada = ""
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
        os.system("cls")
        print("( 1 ) - PLAY ")
        print("( 2 ) - EXIT \n")

        escolha = input(">> ")
        while True:    
            if escolha == "1":
                os.system("cls")

                self.palavra_chave = input("ESCOLHA A PALAVRA CHAVE: ")
                self.palavra_list = self.palavra_chave
                self.palavra_chave_list = ["_"] * len(self.palavra_chave)
                break
                
            if escolha == "2":
                break

        self.starttogame()
        os.system("cls")


    def starttogame(self):
        while True:
            if self.error == 7:
                break
            if self.error == 6:
                print("VOCÊ PERDEU KK")
                escolha_repeticao = input("VOCÊ DESEJA REPETIR(SIM/NÃO): ")
                if escolha_repeticao.upper() == "SIM" or escolha_repeticao.upper() == "S":
                   
                    os.system("cls")
                    self.error = 0
                    self.palavra_list = ""
                    self.palavra_digitada = ""
                    self.options()

                else:
                    os.system("pause")
                    break

            else:        
                self.bonecao_mandraki = Boneco()
                self.bonecao_mandraki.exibir_forca(self.error)
                print(" "*25, " ".join(self.palavra_chave_list))
                print("\n", " "*25, "PALAVRAS JÁ DIGITADAS: ", self.palavra_digitada)

                print("\nDIGITE A LETRA QUE DESEJA: ", end="")
                letra = input("")

                os.system("cls")
                self.verificar(letra)
                    

    def verificar(self, letra):
        if len(letra) == 1:
            confirm_action = False
            self.palavra_digitada = str(self.palavra_digitada + "|" +letra)

            for i, j in enumerate(self.palavra_list):
                if letra.upper() == j.upper():
                    confirm_action = True
                    self.palavra_chave_list[i] = letra

            if confirm_action == False:
                self.error += 1
                os.system("cls")

            if "_" not in self.palavra_chave_list:
                self.error = 7
                os.system("cls")
                print("TA ESPERTO EIN, PARABENS A PALAVRA ERA:", "".join(self.palavra_chave_list))

                escolha_repeticao = input("VOCÊ DESEJA REPETIR(SIM/NÃO): ")
                if escolha_repeticao.upper() == "SIM" or escolha_repeticao.upper() == "S":
                    os.system("cls")
                    self.error = 0
                    self.palavra_list = ""
                    self.palavra_digitada = ""
                    self.options()
                
        else:
            os.system("cls")
            print("FAVOR DIGITAR UM CARACTER!")
            os.system("pause")
            os.system("cls")
            self.starttogame()