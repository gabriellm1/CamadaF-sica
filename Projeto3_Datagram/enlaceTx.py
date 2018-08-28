#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Threads
import threading

# Class
class TX(object):
    """ This class implements methods to handle the transmission
        data over the p2p fox protocol
    """

    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.transLen    = 0
        self.empty       = True
        self.threadMutex = False
        self.threadStop  = False


    def thread(self):
        """ TX thread, to send data in parallel with the code
        """

        
        while not self.threadStop:
            if(self.threadMutex):
                #inicia contador de tempo
                start_time = time.time()
                self.transLen    = self.fisica.write(self.buffer)
                print("O tamanho transmitido, impressao de dentro do thread {}" .format(self.transLen))
                self.threadMutex = False
                #indica o tempo da transmissão
                print("-------------------------")
                print("--- levou %s segundos para transmitir ---" % (time.time() - start_time))
                print("-------------------------") 

    def threadStart(self):
        """ Starts TX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()


    def threadKill(self):
        """ Kill TX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the TX thread to run

        This must be used when manipulating the tx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the TX thread (after suspended)
        """
        self.threadMutex = True

    def sendBuffer(self, data):
        """ Write a new data to the transmission buffer.
            This function is non blocked.

        This function must be called only after the end
        of transmission, this erase all content of the buffer
        in order to save the new value.
        """
        self.transLen   = 0
        #empacotamento
        head = ((len(data)).to_bytes(10, byteorder='big'))
        EOP = bytes('vtncgv','utf-8')



        #EOP proposital
        data = data[:500]+EOP+data[500:] 


        
        #bytestuffing
        stuff = bytes('P','utf-8')
        for i in range(len(data)-5):
            if data[i:i+6] == EOP:
                data = data[:i]+stuff+data[i:]
                break
            else:
                pass


               


        self.buffer = b''.join([head, data,EOP])

        print("-------------------------")
        print("Overhead: {} ".format((len(self.buffer))/(len(data))))
        print("-------------------------")

        print("-------------------------")
        print("Throughput: {} ".format((len(self.buffer))/(self.fisica.baudrate)))
        print("-------------------------") 

        self.threadMutex  = True

    def getBufferLen(self):
        """ Return the total size of bytes in the TX buffer
        """

        return(len(self.buffer))

    def getStatus(self):
        """ Return the last transmission size
        """
        #print("O tamanho transmitido. Impressao fora do thread {}" .format(self.transLen))
        return(self.transLen)
        

    def getIsBussy(self):
        """ Return true if a transmission is ongoing
        """
        return(self.threadMutex)

