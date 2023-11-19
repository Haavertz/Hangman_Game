from boneco import Boneco
import time
import os

class MyGameHangman():
    def __init__(self) -> None:
        self.error = 0 
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
                break
                
            if escolha == "2":
                break

        os.system("cls")
        self.starttogame()


    def starttogame(self):
        try:        
            self.boneco1 = Boneco()
            self.boneco1.exibir_forca(self.error)
            print("DIGITE A LETRA QUE DESEJA: ", end="")
            letra = input("")
            self.verificar(letra)
            
        except:
            self.gamestop

    def verificar(self, letra):
        if len(letra) == 1:
            for j in self.palavra_chave:
                if letra == j:
                    print(self.palavra_chave, letra)
                else:
                    os.system("cls")
                    self.error += 1
                    self.starttogame()
        else:
            print("POR FAVOR, DIGITE APENAS UM CARACTER.")
        

    def gamestop(self):
        print("VOCÊ PERDEU O GAME KKKKK")


MyGameHangman()