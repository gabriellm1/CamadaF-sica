print("start - TX")

from enlace import *
from graphic import findimg
import time

serialName = "COM7" 



def main():
    # Inicializa enlace 
    com = enlace(serialName)
    print("porta COM7 aberta com sucesso")

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação com transmissor aberta")



    print ("gerando dados para transmissao :")
  



    with open(findimg(), "rb") as imageFile:
      baby = imageFile.read()
      
      txBuffer = bytearray(baby)

    txLen = len(txBuffer) 
    #print(txLen) 


    #previsão de tempo de transmissão
    bdr = com.tx.fisica.baudrate
    print("-------------------------")
    print("Previsão de tempo para tranmissão: {} segundos".format(txLen*16/bdr))
    print("-------------------------")

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))


    com.sendData(txBuffer)



    
    #print(txBuffer)
        
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus() 





    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
