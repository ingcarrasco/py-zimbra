"""
Autor: Angel Carrasco
Fecha: 8 de Marzo de 2024
"""
#start time:- 2024-03-08 13:46:35.874170
#end time:- 2024-03-08 13:54:15.228587
import datetime
# Libreria de funciones personalizadas de zmprov
from addmembers import *

# El diccionario es done encontraremos el catalogo de domain, building, brand, region and distribution list
from dictionary import *

ct = datetime.datetime.now()
print("current time:-", ct)

for x in myDict:
    # Valores de todos los dominios en el diccionario
    # print ("Dominio: " + myDict[x][0] + "\nListaRegion: " + myDict[x][1] + "\nListaMarca: " + myDict[x][2] + "\nListaDomino: " + myDict[x][3] + '\n')
    # Todos los correos que pertenecen al dominio y la region
    addmemberstolist(myDict[x][0],myDict[x][1])
    # Todos los correos que pertenecen al dominio y la region
    addmemberstolist(myDict[x][0],myDict[x][2])
    # Todos los correos que pertenecen al dominio y la region
    addmemberstolist(myDict[x][0],myDict[x][3])

# sprint (search_mail(myDict[x][0]))
        
# print('Dominio: *' + '\nLista: comunicado.interno@gruposolana.com')

addmemberstolist()

ct = datetime.datetime.now()
print("current time:-", ct)