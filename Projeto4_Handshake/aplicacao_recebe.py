print("start - RX")

from enlace import *
import time

serialName = "COM7"


def main():

    # Inicializa enlace 
    com = enlace(serialName)
    print("porta COM7 aberta com sucesso") 
    # Ativa comunicacao
    
    com.enable()

    #verificar que a comunicação foi aberta
    print("comunicação com recebedor aberta")


    #ETAPA 1

    bnone = bytes(10)
    one , head1 , payload1 , payloadsize1 = only_listen(1)
    com.sendData(2,bnone)
    print("----Tipo 2 enviada, aguardando 3----")
    three , head3 , payload3  = listen_and_tell(2,bnone,3)




    #ETAPA 2
    four , head4 , payload4 , payloadsize4 = only_listen(4)
    ##consistência

    if (int.from_bytes(head[7], byteorder='big'))!=payloadsize4:
        com.sendData(6,bnone)
        print("----Tipo 6 enviada----")
    else:
        com.sendData(5,bnone)
        print("----Tipo 5 enviada----")



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



    head, rxBuffer, nRx = com.getData(bytesSeremLidos)
    #print(rxBuffer)

    # log
    print ("Lido              {} bytes ".format(nRx))
    





    # Le a imagem retornada do loop
    new = open("imagens/newimg.jpg", "wb") 
    new.write(content) 
    new.close()


    # Encerra comunicação
    print("-------------------------")
    print("Imagem salva")
    print("-------------------------")

    seven , head7 , payload7 , payloadsize7 = only_listen(7)
    print("Solicitação de encerramento aceita")
    com.disable()


    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
