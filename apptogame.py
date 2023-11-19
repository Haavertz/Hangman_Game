from boneco import Boneco
import time

class MyGameHangman():
    def __init__(self) -> None:
        self.exibir_boas_vindas()

    def exibir_boas_vindas(self):
        print("","-="*17, end="-\n")
        time.sleep(0.3)
        print("-=   BEM-VINDO AO GAME DA FORCA!   =-", end="\n")
        time.sleep(0.3)
        print("-=                                 =-", end="\n")
        time.sleep(0.3)
        print("-=    Vamos começar a diversão!    =-", end="\n")
        time.sleep(0.3)
        print("-=    Tente adivinhar a palavra    =-", end="\n")
        time.sleep(0.3)
        print("-=    antes que o boneco seja      =-", end="\n")
        time.sleep(0.3)
        print("-=    completamente desenhado.     =-", end="\n")
        time.sleep(0.3)
        print("-=                                 =-", end="\n")
        time.sleep(0.3)
        print("-=           GOOD LUCK!            =-", end="\n")
        print("","-="*17, end="-\n")




MyGameHangman()