from enlace import *
import time

def listen_and_tell(tipo_envia,content,tipo_recebe):

	tipo_recebido = 0
    while tipo_recebe != tipo_recebido:

	    pack=com.rx.getBufferLen()
	    start_time = time.time()

	    k=10
	    while (pack != k or pack==0) :
			
			temp = time.time() - start_time

			if temp < 5 or pack !=0: 	
		        k = pack
		        pack=com.rx.getBufferLen()
		        time.sleep(1)
		        print("Aguardando dados")
		        print(pack)

		    else:
		    	start_time = time.time()
		    	com.sendData(tipo_envia,content)
		    	print("Mensagem tipo {} não recebida".format(tipo_recebe))
		    	print(". . . Recontatando . . .")

		head , payload, payloadsize = com.getData(pack)
		tipo_recebido = int.from_bytes(head[7], byteorder='big')

		if tipo_recebe != tipo_recebido:
			print("Mensagem de tipo inesperado recebida") 


return tipo_recebido, head, payload



def only_listen(tipo_recebe):

	tipo_recebido = 0
    while tipo_recebe != tipo_recebido:

	    pack=com.rx.getBufferLen()
	    start_time = time.time()

	    k=10
	    while (pack != k or pack==0) :
			
			temp = time.time() - start_time

			if temp < 5 or pack !=0: 	
		        k = pack
		        pack=com.rx.getBufferLen()
		        time.sleep(1)
		        print("Aguardando dados")
		        print(pack)

		    else:
		    	start_time = time.time()
		    	print("Mensagem tipo {} não recebida".format(tipo_recebe))
		    	print(". . . Aguardando . . .")

		head , payload, payloadsize = com.getData(pack)
		tipo_recebido = int.from_bytes(head[7], byteorder='big')

		if tipo_recebe != tipo_recebido:
			print("Mensagem de tipo inesperado recebida") 


return tipo_recebido, head, payload , payloadsize


def listen_and_tell_double(tipo_envia,content,tipo_recebe1,tipo_recebe2):

	tipo_recebido = 0
    while (tipo_recebe1 != tipo_recebido) and (tipo_recebe2 != tipo_recebido):

	    pack=com.rx.getBufferLen()
	    start_time = time.time()

	    k=10
	    while (pack != k or pack==0) :
			
			temp = time.time() - start_time

			if temp < 5 or pack !=0: 	
		        k = pack
		        pack=com.rx.getBufferLen()
		        time.sleep(1)
		        print("Aguardando dados")
		        print(pack)

		    else:
		    	start_time = time.time()
		    	com.sendData(tipo_envia,content)
		    	print("Mensagem tipo {} ou {} não recebida".format(tipo_recebe1,tipo_recebe2))
		    	print(". . . Recontatando . . .")

		head , payload, payloadsize = com.getData(pack)
		tipo_recebido = int.from_bytes(head[7], byteorder='big')

		if (tipo_recebe1 != tipo_recebido) and (tipo_recebe2 != tipo_recebido):
			print("Mensagem de tipo inesperado recebida") 


return tipo_recebido, head, payload








# tipo2_received = False
# bnone = bytes(10)

# while(not tipo2_received):
#     com.sendData(1,bnone)
#     start_time = time.time()
    
#     k=50
#     tipo2=com.rx.getBufferLen()
#     while (tipo2 != k or tipo2==0) :
#         if((time.time() - start_time)>5 and tipo2==0):
#                 print("Tipo 1 não encontrada, recontatando server")
#                 break
#         else:        
#             k = bytesSeremLidos
#             tipo2=com.rx.getBufferLen()
#             time.sleep(0.5)
#             print("Contatando Server . . . {} bytes recebidos".format(tipo2))  
#     head,bnone2, nNone = com.getData(tipo2)
#     if(int.from_bytes(head[7], byteorder='big') == 2):
#         tipo2_received = True
#         com.sendData(3,bnone)
#         print("Server me ouve")
#     else:
#         print("Tipo 2 não encontrada, recontatando server")

# #ETAPA 1
# print ("Iniciando contato .... ")
# tipo1_received = False
# tipo3_received = False
# bnone = bytes(10)
# while(not tipo1_received)
#     k=10
#     bytesSeremLidos=com.rx.getBufferLen()
#     while (bytesSeremLidos != k or bytesSeremLidos==0) :
#         k = bytesSeremLidos
#         bytesSeremLidos=com.rx.getBufferLen()
#         time.sleep(1)
#         print(bytesSeremLidos)
#         print("Aguardando dados")
#     head, rxBuffer, nRx = com.getData(bytesSeremLidos)
#     if int.from_bytes(head[7], byteorder='big') == 1 :
        
#         tipo1_received = True
#         print("Cliente quer me contatar")
#     else:
#         print("Tipo 1 corrimpida ou inesistente")

# while(not tipo3_received):
#     com.sendData(2,bnone)
#     start_time = time.time()
    
#     k=50
#     tipo2=com.rx.getBufferLen()
#     while (tipo2 != k or tipo2==0) :
#         if((time.time() - start_time)>5 and tipo2==0):
#                 print("Tipo 1 não encontrada, recontatando server")
#                 break
#         else:        
#             k = bytesSeremLidos
#             tipo2=com.rx.getBufferLen()
#             time.sleep(0.5)
#             print("Contatando Server . . . {} bytes recebidos".format(tipo2))  
#     head,bnone2, nNone = com.getData(tipo2)
#     if(int.from_bytes(head[7], byteorder='big') == 2):
#         tipo2_received = True
#         com.sendData(3,bnone)
#         print("Server me ouve")
#     else:
#         print("Tipo 2 não encontrada, recontatando server")
