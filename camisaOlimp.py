tamP = 0
tamM = 0
tamCam = 0
resp = ''

numPrem = int(input("")) #numeros de premiados
tam = input("").split(" ") #tamanhos das camisas dos premiados
prodP = int(input("")) #camisas tamanho P
prodM = int(input("")) #camisas do tamaho M

for i in range(len(tam)):
    tam[i] = int( tam[i])
    if(tam[i] == 1):
        tamP += 1
    else:
        tamM += 1
    if(tamP == prodP and tamM == prodM):
        resp = 'S'
    else:
        resp = 'N'
        
print(resp)

   