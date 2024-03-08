# Aqui encontramos las claves de acceso
from access import zmprov
# El modulo zmprov para ejecutar el CLI de Zimbra
from ozpy.zmprov import Zmprov
from dictionary import allmail

def search_mail(search=None):
    """Regresa todos los correos que tengan la palabra deseada, por ejemplo un dominio o parte del mismo correo.

    Args:
        search (str): optional
            Default es igual a None, lo cual nos trae todos los correos

    Returns:
        return (list):
            Regresa la lista de correos buscados
    """
    # Ejecuta la funcion Get All Accouunt de la clase zmprov y trae todos los correos
    all_mails = zmprov.gaa()
    # Aqui se filtran los valores y se retornan
    result = []
    if not search:
        result = all_mails
        pass
    else:
        for s in all_mails:
            if search in s:
                result.append(s)
    return result

def search_dl(search):
    all_dl = zmprov.gadl()
    result = []
    for s in all_dl:
        if search in s:
            result.append(s)
    return result

def addmemberstolist(domain=None,dlist=None):
    """Agrega todos los correos segun los filtros seleccionados a la listas de distribucion.

    Args:
        domain (str): Opcional
            especificamos
        distlist (str): _description_

    Returns:
        _type_: _description_
    """
    if domain!=None:
        result = search_dl(dlist)

        if len(result) > 0:
            dlist = zmprov.gdlcheck(dlist)
            members = search_mail(domain)
            zmprov.adlm(dlist,members)
        else:
            print ('NO EXISTE' + dlist + '\n Acaba de ser creada la lista...\n')
            zmprov.cdl(dlist)
            dlist = zmprov.gdlcheck(dlist)
            members = search_mail(domain)
            zmprov.adlm(dlist,members)
    else:
        dlist = zmprov.gdlcheck(allmail)
        members = search_mail()
        zmprov.adlm(dlist,members)
        
    return 0
