print("start - RX")

from enlace import *
import time

serialName = "COM7"


def main():

    # Inicializa enlace 
    com = enlace(serialName)
    print("porta COM7 aberta com sucesso") 
    # Ativa comunicacao
    #com.disable() #rodar uma vez caso porta esteja bloqueada
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação com recebedor aberta")

    #previsão de tempo de transmissão
    bdr = com.tx.fisica.baudrate
    print("-------------------------")
    print("Previsão de tempo para recebimento: {} segundos".format(7456*16/bdr))
    print("-------------------------")

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")


    k=10
    bytesSeremLidos=com.rx.getBufferLen()
    while (bytesSeremLidos != k or bytesSeremLidos==0) :
        k = bytesSeremLidos
        bytesSeremLidos=com.rx.getBufferLen()
        time.sleep(1)
        print(bytesSeremLidos)
        print("Aguardando dados")    



    rxBuffer, nRx = com.getData(bytesSeremLidos)
    #print(rxBuffer)

    # log
    print ("Lido              {} bytes ".format(nRx))
    
    

    # Le a imagem retornada do loop
    new = open("imagens/newimg.jpg", "wb") 
    new.write(rxBuffer) 
    new.close()


    # Encerra comunicação
    print("-------------------------")
    print("Imagem salva - comunicação encerrada")
    print("-------------------------")
    com.disable()


    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
