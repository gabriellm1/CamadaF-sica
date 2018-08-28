print("start - TX")

from enlace import *
from graphic import findimg
import time
from identify import *

serialName = "COM7" 



def main():
    # Inicializa enlace 
    com = enlace(serialName)
    print("porta COM7 aberta com sucesso")

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação com transmissor aberta")


    #ETAPA 1 ##########################################

    bnone = bytes(10)
    com.sendData(1,bnone)
    print("----Tipo 1 enviada, aguardando 2----")
    two , head2 , payload2 = listen_and_tell(1,bnone,2)
    com.sendData(3,bnone)

    ###################################################



    # ETAPA2 ########################################################################

    print ("gerando dados para transmissao :")

    with open(findimg(), "rb") as imageFile:
      baby = imageFile.read()
      
      txBuffer = bytearray(baby)

    txLen = len(txBuffer)

    


    #previsão de tempo de transmissão
    bdr = com.tx.fisica.baudrate
    print("-------------------------")
    print("Previsão de tempo para tranmissão: {} segundos".format(txLen*16/bdr))
    print("-------------------------")

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))



    com.sendData(4,txBuffer)
    print("----Tipo 4 enviada, aguardando 5 ou 6----")
    fivesix , head56 , payload56 = listen_and_tell_double(4,txBuffer,5,6)
   
       
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()

    ################################################################################


    #ETAPA 3
    com.sendData(7,bnone)
    print("Encerramento solicitado") 
    com.disable()




    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
