import lista_doppia_conc
import pickle
from lista_posizionale_dopp_conc import *
from UnsortedTableMap import *
from Heap import *
from LinkedBinaryTree import *
import random
from ArrayStack import *

global libreria
libreria = UnsortedTableMap()
supporto = UnsortedTableMap()
scaffale = [[] for bucket in range(6)]
global utenti
utenti = PositionalList()
global ordinamento
ordinamento = HeapPriorityQueue()
global albero
albero = LinkedBinaryTree()
global cronologia
cronologia = ArrayStack()

if utenti.first() is None:
    global riferimento
    cod_rif = 50
    cod_nom = "RIFERIMENTO"
    cod_rif = str(cod_rif)
    riferimento = cod_nom + " " + cod_rif
    pos = utenti.add_first(riferimento)
"""
--------------------------------------------------------------------------------------METODI MAPPA
"""
def esiste_libro(richiesta):
        """
        Controlla se esiste un libro e restituisce un booleano.         ---Complessità algoritmo: O(1)---
        :param richiesta:
        :return:
        """
        i = iter(libreria)
        libro = nome_libro
        id = int(id_libro)
        if id in libreria.keys():
            for i in libreria:
                if libreria[i] == libro:
                    return True
        return False

def aggiungi_libro():
    """
        Aggiunge un libro in mappa e in base alla chiave aggiunge in hash_map.       ---Complessità algoritmo: O(1)---
    """
    v = str((input("Titolo del libro da aggiungere: ")))
    k = int((input(" Definisci l'ID(0-60): ")))
    libreria[k] = v
    if k <= 10:
        hash_key = 0
    elif k > 10 and k <= 20:
        hash_key = 1
    elif k > 20 and k <= 30:
        hash_key = 2
    elif k > 30 and k <= 40:
        hash_key = 3
    elif k > 40 and k <= 50:
        hash_key = 4
    elif k > 50 and k <= 60:
        hash_key = 5
    try:
        insert(scaffale, k, v, hash_key)
        print("Posizionamento libro nello scaffale.....\nAttendere\n")
        save_obj(libreria, "libreria")
    except:
        print("ID fuori dal range.")

def vedi_tutti_libri():
    """
        Visualizza tutti gli elementi della mappa.           ---Complessità algoritmo: O(1)---
    :return:
    """
    i = iter(libreria)
    for i in libreria:
        print(libreria[i])

def rimuovi_libro(k):
    """
       Permette la cancellazione di un libro dalla mappa e da hash_map.         ---Complessità algoritmo: O(1)---
    :return:
    """
    delete(scaffale, k)
    del libreria[k]
    save_obj(libreria, "libreria")

"""
--------------------------------------------------------------------------------------METODI HASH TABLE
"""
def insert(scaffale, key, value, hash_key):
    """
        Metodo chiamato da AGGIUNGI_LIBRO per inserimento in hash_table.            ---Complessità algoritmo: O(1)---
    :param hash_table:
    :param key:
    :param value:
    :param hash_key:
    :return:
    """
    key_exists = False
    bucket = scaffale[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
    print(scaffale)
    save_obj(scaffale, "scaffali")

def vedi_per_reparto():
    """
        Permette la visualizzazione per reparto (bucket).               ---Complessità algoritmo: O(1)---
    """
    print("\nReparto 0: Filosofia\nReparto 1: Informatica\nReparto 2: Psicologia\nReparto 3: Scienze Motorie\nReparto 4: Lingue e Culture Moderne\nReparto 5: Astrologia")
    i = int(input("\n Quale reparto vuoi visualizzare? : "))
    try:
        if len(scaffale[i]) == 0:
            scelta2 = int(input("\n\n ***Lo scaffale è vuoto.*** \n Digita 0 per uscire. \n Digita un altro numero per continuare la ricerca : "))
            if scelta2 != 0:
                vedi_per_reparto()
            elif scelta2 == 0:
                cancella_albero()
        else:
            print(scaffale[i])
    except:
        print("Scaffale non presente.")
        vedi_per_reparto()

def delete(scaffale, k):
    """
        Metodo chiamato da RIMUOVI_LIBRO per eliminare in hash_table.           ---Complessità algoritmo: O(1)---
    :param scaffale:
    :param k:
    :return:
    """
    if k <= 10:
        hash_key = 0
    elif k > 10 and k <= 20:
        hash_key = 1
    elif k > 20 and k <= 30:
        hash_key = 2
    elif k > 30 and k <= 40:
        hash_key = 3
    elif k > 40 and k <= 50:
        hash_key = 4
    elif k > 50 and k <= 60:
        hash_key = 5

    key_exists = False
    bucket = scaffale[hash_key]
    for i, kv in enumerate(bucket):
        k1, v = kv
        if k == k1:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(k))
    else:
        print ('Key {} not found'.format(k))
    save_obj(scaffale, "scaffali")
"""
--------------------------------------------------------------------------------------METODI PICKLE
"""
def save_obj(obj, name):
    """
        Metodo per salvare una struttura dati in binario su file.           ---Complessità algoritmo: O(1)---
    :param obj:
    :param name:
    """
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    """
        Metodo per acquisire da file.               ---Complessità algoritmo: O(1)---
    :param name:
    """
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

"""
--------------------------------------------------------------------------------------METODI LISTA POSIZIONALE
"""
def inserimento():
    """
        Consente di riempire i campi nome, codice e in base a quest'ultimo inoltra ad INSERIMENTO_GOLD o ad INSERIMENTO_SILVER.             ---Complessità algoritmo: O(N)---
    :return:
    """
    nome = str(input("Inserisci il nome della persona: "))
    codice = int(input("Inserisci il codice: "))
    codice1 = str(codice)
    nome1 = nome + " " + codice1
    cod_rif = 50
    cod_nom = "RIFERIMENTO"
    cod_rif = str(cod_rif)
    riferimento = cod_nom + " " + cod_rif
    if int(codice1) < 50:
        inserimento_gold(nome1, riferimento)
    else:
        inserimento_silver(nome1, riferimento)
    save_obj(utenti, "Lista_utenti")

def inserimento_gold(persona, riferimento):
    """
        Metodo che permette di inserire una persona prima del riferimento.              ---Complessità algoritmo: O(N)---
    :param persona:
    :param riferimento:
    :return:
    """
    cursore = utenti.last()
    while cursore is not None:
        if utenti.get_element(cursore) == riferimento:
            cursore = utenti.add_before(cursore, persona)
        cursore = utenti.before(cursore)
    cursore = utenti.last()
    while cursore is not None:
        print(cursore.element())
        cursore = utenti.before(cursore)

def inserimento_silver(persona, riferimento):
    """
        Metodo che permette di inserire una persona dopo del riferimento.               ---Complessità algoritmo: O(N)---
    :param persona:
    :param riferimento:
    :return:
    """
    cursore = utenti.first()
    while cursore is not None:
        if utenti.get_element(cursore) == riferimento:
            cursore = utenti.add_after(cursore, persona)
        cursore = utenti.after(cursore)
    cursore = utenti.first()
    while cursore is not None:
        print(cursore.element())
        cursore = utenti.after(cursore)

def verifica_priorita_gold(persona):
    """
        Verifica se una persona si trova prima di RIFERIMENTO.              ---Complessità algoritmo: O(N)---
    :param persona:
    :return:
    """
    cursore = utenti.first()
    while "RIFERIMENTO" != utenti.get_element(cursore):
        if persona == utenti.get_element(cursore):
            return True
        else:
            cursore = utenti.after(cursore)
    return None

def cerca_in_lista(persona):
    """
        Verifica se una persona è in lista ed eventualmente ne ritorna la posizione.            ---Complessità algoritmo: O(N)---
    :param persona:
    :return:
    """
    cursore = utenti.first()
    while cursore is not None:
        if utenti.get_element(cursore) == persona:
            return cursore
        else:
            cursore = utenti.after(cursore)

    cursore = utenti.last()
    while cursore is not None:
        if utenti.get_element(cursore) == persona:
            return cursore
        else:
            cursore = utenti.before(cursore)
    return None

def rimuovi_da_lista(persona):
    """
        Rimuove e restituisce la posizione dell'elemento eliminato.             ---Complessità algoritmo: O(N)---
    :param persona:
    :return:
    """
    cursore = utenti.first()
    while cursore is not None:
        if utenti.get_element(cursore) == persona:
            print("\nUtente" + " " + persona + " " + "rimosso con successo!\n")
            return utenti.delete(cursore)
        else:
            cursore = utenti.after(cursore)
    print("\nUtente non trovato!\n")
    return None

def visualizza_lista():
    """
        Visualizza tutti gli elementi della Lista.          ---Complessità algoritmo: O(N)---
    :return:
    """
    cursore = utenti.first()
    while cursore is not None:
        print(cursore.element())
        cursore = utenti.after(cursore)

def cancella_da_lista():
    """
        Raccoglie i dati della persona da cancellare e, se esiste, ne inoltra i dati a RIMUOVI_DA_LISTA.            ---Complessità algoritmo: O(N)---
    :return:
    """
    visualizza_lista()
    nome = str(input("Inserisci il nome del profilo da eliminare: "))
    codice = int(input("Inserisci il codice: "))
    codice = str(codice)
    nome = nome + " " + codice
    risultato = rimuovi_da_lista(nome)

    if risultato is None:
        print("Profilo non presente")
    else:
        print(risultato + "è stato rimosso con successo")
        if int(codice) < 50:
            print("°°°UTENTE GOLD°°°")
        else:
            print("°°°UTENTE SILVER°°°")
        save_obj(utenti, "Lista_utenti")
"""
--------------------------------------------------------------------------------------METODI HEAP/CODA PRIORITARIA  
"""
def aggiungi_alla_coda(ordine):
    """
        Metodo che dato il parametro di tipo str concatenata 'ordine' ne preleva nome e id,
        verifica prima se è presente in lista ed eventualmente se ha abbonamento gold ed assegna una certa priorità.                ---Complessità algoritmo: O(N)---
    :param ordine:
    :return:
    """
    nome1, id1,x,y = ordine.split()
    utente1 = nome1 + " " + id1
    print("****************")
    print(utente1)
    controllo = cerca_in_lista(utente1)
    if int(id1) < 50:
        ordinamento.add(len(ordinamento) + 1, ordine)
    elif int(id1) < 100:
        ordinamento.add(len(ordinamento) + 50, ordine)
    else:
        ordinamento.add(len(ordinamento) + 100, ordine)
    save_obj(ordinamento, "Request")

def raccogli_richiesta(persona):
    """
        Metodo che concatena il titolo del libro e il rispettivo id al paramentro in entrata, verifica se il libro esiste ed eventualmente inoltra l'ordine ad AGGIUNGI_ALLA_CODA.        ---Complessità algoritmo: O(N)---
    :param persona:
    :return:
    """
    global id_libro, nome_libro
    semaforo1 = 0
    nome1, codice2 = persona.split()
    while semaforo1 == 0:
        nome_libro = str(input("\nTitolo del libro desiderato: "))
        id_libro = int(input("\nInserisci il codice libro: "))
        id_libro1 = str(id_libro)
        richiesta = nome_libro + " " + id_libro1
        controllo1 = esiste_libro(richiesta)
        if controllo1 is True:
            ordine = nome1 + " " + codice2 + " " + nome_libro + " " + id_libro1
            aggiungi_alla_coda(ordine)
            semaforo1 = 1
        else:
            esci = int(input("Il libro non esiste, digita 1 per riprovare, 0 per uscire "))
            if esci == 0:
                semaforo1 = 1
            else:
                vedi_per_reparto()

"""
------------------------------------------------------------------------------METODI PILA
"""
def visualizza_cronologia():
    """
        Svuota la pila permettendo la visualizzazione spostando gli elementi in un array. Questi vengono poi riaggiunti alla pila.          ---Complessità algoritmo: O(N)---perchè la lungheza della cronologia non è nota a priori
    :return:
    """
    if cronologia.is_empty() is True:
        print("Cronologia vuota")
    for i in range(len(cronologia)):
        supporto[i] = cronologia.pop()
        print(supporto[i])
    if cronologia.is_empty() is True:
        for i in range(len(supporto)):
            cronologia.push(supporto[i])

def cancella_cronologia():
    """
        Cancella il contenuto della pila.           ---Complessità algoritmo: O(N)---perchè la lungheza della cronologia non è nota a priori
    :return:
    """
    if cronologia.is_empty() is True:
        print("La cronologia è vuota\n")
    else:
        for i in range(len(cronologia)):
            cronologia.pop()
        save_obj(cronologia, "Cronologia")
        print("Cronologia Cancellata.\n")

"""
-------------------------------------------------------------------------------METODI DI SUPPORTO
"""
def gestisci_richiesta():
    """
        Preleva una richiesta dalla coda, sfruttando la concatenazione di UTENTE preleva il campo ID ed elimina il libro da hash_map, mappa e inserisce la richiesta nella pila.        ---Complessità algoritmo: O(1)---
    :return:
    """
    prova = 0
    try:
        cancellato = ordinamento.remove_min()
        print(cancellato)
        cronologia.push(cancellato)
        save_obj(ordinamento, "Request")
        save_obj(cronologia, "Cronologia")
        a = cancellato[-1]
        b, c, d, z = a.split()
        print(z)
        x = int(z)
    except:
        print("\nNessuna richiesta in coda!\n")
        prova = 1
    if prova != 1:
        try:
            rimuovi_libro(x)
        except:
            print("\nIl libro è già stato venduto.")
            cronologia.pop()
            save_obj(cronologia, "Cronologia")

#--------------------------------------------------------------------------------------METODI MAIN
def menu_benvenuto():
    accesso = int((input("Digita: \n1)Entra come amministratore \n2)Entra come cliente \n3)Esci \n------>")))
    return accesso

def cancella_albero():
    """
        Metodo utilizzato per rimuovere tutti i nodi dell'albero.
    :return:
    """
    if albero.root() is not None:
        try:
            albero.delete(figlio21)
            print("Nodo 21 eliminato")
        except:
            None
        try:
            albero.delete(figlio19)
            print("Nodo 19 eliminato")
        except:
            None
        try:
            albero.delete(figlio18)
            print("Nodo 18 eliminato")
        except:
            None
        try:
            albero.delete(figlio16)
            print("Nodo 16 eliminato")
        except:
            None
        try:
            albero.delete(figlio15)
            print("Nodo 15 eliminato")
        except:
            None
        try:
            albero.delete(figlio14)
            print("Nodo 14 eliminato")
        except:
            None
        try:
            albero.delete(figlio10)
            print("Nodo 10 eliminato")
        except:
            None
        try:
            albero.delete(figlio9)
            print("Nodo 9 eliminato")
        except:
            None
        try:
            albero.delete(figlio6)
            print("Nodo 6 eliminato")
        except:
            None
        try:
            albero.delete(figlio5)
            print("Nodo 5 eliminato")
        except:
            None
        try:
            albero.delete(figlio4)
            print("Nodo 4 eliminato")
        except:
            None
        try:
            albero.delete(figlio3)
            print("Nodo 3 eliminato")
        except:
            None
        try:
            albero.delete(figlio2)
            print("Nodo 2 eliminato")
        except:
            None
        try:
            albero.delete(figlio1)
            print("Nodo 1 eliminato")
        except:
            None

#---------------------------------------------------------------------------------METODI AMMINISTRATORE
def menu_amministratore():
    accesso = int((input("Menu Amministratore: \n1) Aggiungi Libro o Utente \n2) Gestisci \n------>")))
    return accesso

def aggiungi_qualcosa():
    accesso = int((input("Menu Amministratore: \n1) Aggiungi un Libro \n2) Registra Utente \n------>")))
    return accesso

def menu_gestisci():
    accesso = int((input("Menu Amministratore: \n1) Visualizza o Elimina Libri \ Utenti \n2) Gestisci Richieste \ Cronologia Vendite \n------>")))
    return accesso

def menu_visualizza_elimina():
    accesso = int((input("Menu Amministratore: \n1) Visualizza \n2) Elimina \n------>")))
    return accesso

def menu_visualizza_amm():
    accesso = int((input("Menu Amministratore: \n1) Visualizza Libri \n2) Visualizza Utenti \n------>")))
    return accesso

def menu_elimina():
    accesso = int((input("Menu Amministratore: \n1) Elimina libro \n2) Elimina utente \n------>")))
    return accesso

def menu_servizi():
    accesso = int((input("Menu Amministratore: \n1) Servi cliente in coda \n2) Cronologia delle vendite \n------>")))
    return accesso

def menu_cronologia():
    accesso = int((input("Menu Amministratore: \n1) Visualizza cronologia \n2) Resetta cronologia \n------>")))
    return accesso

#-----------------------------------------------------------------------METODI UTENTE
def menu_utente():
    accesso = int((input("Menu Utente: \n1) Visualizza Catalogo \n2) Fai una richiesta \n------>")))
    return accesso

def menu_visualizza():
    accesso = int((input("Menu Utente: \n1) Visualizza tutto \n2) Visualizza per reparto \n------>")))
    return accesso

def menu_ordine():
    accesso = int((input("Menu Utente: \n1) Effettua il log-in \n2) Prosegui come utente normale \n------>")))
    return accesso

def menu_non_abbonati():
    accesso = int((input("Menu Utente: \n1) Registrati \n2) Prosegui senza iscrizione \n------>")))
    return accesso

def menu_tipo_abbonamento():
    accesso = int((input("Menu Utente: \n1) UTENTE GOLD (Sarai fra i primi ad essere servito) \n2) UTENTE SILVER (Sarai servito prima dei non-abbonati) \n------>")))
    return accesso

if __name__ == "__main__":
    cancella_albero()
    menu = True
    try:
        libreria = load_obj("libreria")
        scaffale = load_obj("scaffali")
        utenti = load_obj("Lista_utenti")
        ordinamento = load_obj("Request")
        cronologia = load_obj("Cronologia")
    except:
        print("I file sono vuoti")

    while menu:
            #------------------------------------------------------------------------------RADICE
        decisione = menu_benvenuto()
        if decisione == 3:
            menu = False
        radice = albero.add_root(decisione)
        prima_scelta = albero.element(radice)

        if prima_scelta == 1:
            #-------------------------------------------------------------------------------------PRIMO_LIVELLO AMMINISTRATORE (AGGIUNGI O GESTISCI)
            decisione = menu_amministratore()
            figlio1 = albero.add_left(radice, decisione)
            scelta = albero.element(figlio1)

            if scelta == 1:
                #--------------------------------------------------------------------------------------SECONDO_LIVELLO AMMINISTRATORE.AGGIUNGI (LIBRO O UTENTE)
                decisione = aggiungi_qualcosa()
                figlio3 = albero.add_left(figlio1, decisione)
                if albero.element(figlio3) == 1:
                    aggiungi_libro()
                elif albero.element(figlio3) == 2:
                    inserimento()

            elif scelta == 2:
                #--------------------------------------------------------------------------------------SECONDO LIVELLO AMMINISTRATORE.GESTISCI(1(1,2),2)
                decisione = menu_gestisci()
                figlio4 = albero.add_right(figlio1, decisione)
                if albero.element(figlio4) == 2:
                    decisione = menu_servizi()
                    figlio10 = albero.add_right(figlio4, decisione)
                    if albero.element(figlio10) == 1:
                        gestisci_richiesta()
                        save_obj(cronologia, "Cronologia")
                    elif albero.element(figlio10) == 2:
                        decisione = menu_cronologia()
                        figlio18 = albero.add_right(figlio10, decisione)
                        if albero.element(figlio18) == 1:
                            visualizza_cronologia()
                        elif albero.element(figlio18) == 2:
                            cancella_cronologia()

                elif albero.element(figlio4) == 1:
                    #------------------------------------------------------------------------------------TERZO LIVELLO AMMINISTRATORE.GESTISCI.1(1,2)
                    decisione = menu_visualizza_elimina()
                    figlio9 = albero.add_left(figlio4, decisione)
                    if albero.element(figlio9) == 1:
                        decisione = menu_visualizza_amm()
                        figlio15 =  albero.add_left(figlio9, decisione)
                        if albero.element(figlio15) == 1:
                            decisione = menu_visualizza()
                            figlio21 = albero.add_left(figlio15, decisione)
                            if albero.element(figlio21) == 1:
                                vedi_tutti_libri()
                            elif albero.element(figlio21) == 2:
                                vedi_per_reparto()

                        elif albero.element(figlio15) == 2:
                            visualizza_lista()

                    elif albero.element(figlio9) == 2:
                        decisione = menu_elimina()
                        figlio16 = albero.add_right(figlio9, decisione)
                        if albero.element(figlio16) == 1:
                            canc = int(input("\nInserisci l'ID del libro da eliminare"))
                            try:
                                rimuovi_libro(canc)
                            except: print("Libro non presente!\n")
                        elif albero.element(figlio16) == 2:
                            visualizza_lista()
                            nome = str(input("\nNome della persona da eliminare: "))
                            codice = int(input("\nCodice della persona da eliminare: "))
                            codice = str(codice)
                            persona = nome + " " + codice
                            rimuovi_da_lista(persona)
                            save_obj(utenti, "Lista_utenti")
                #--------------------------------------------------------------------------------------FINE MENU AMMINISTRATORE

        elif prima_scelta == 2:
            #------------------------------------------------------------------------------------------------MENU CLIENTE
            decisione = menu_utente()
            figlio2 = albero.add_right(radice, decisione)
            scelta2= 1
            if albero.element(figlio2) == 1:
                #------------------------------------------------------------------------------------------------MENU CLIENTE.VISUALIZZA(1,2)
                decisione = menu_visualizza()
                figlio5 = albero.add_left(figlio2, decisione)
                if albero.element(figlio5) == 1:
                    vedi_tutti_libri()
                elif albero.element(figlio5) == 2:
                    while vedi_per_reparto() is False and scelta2!=0:
                        print("Scaffale vuoto!")
                        vedi_per_reparto()



            elif albero.element(figlio2) == 2:
                #-------------------------------------------------------------------MENU CLIENTE.ORDINE(1,2)
                decisione = menu_ordine()
                figlio6 = albero.add_right(figlio2, decisione)
                if albero.element(figlio6) == 1:
                    semaforo = 0
                    tentativi = 0
                    while semaforo == 0:
                        nome = str(input("Inserisci il tuo nome: "))
                        codice = int(input("Inserisci il tuo codice: "))
                        codice1 = str(codice)
                        persona = nome + " " + codice1
                        controllo = cerca_in_lista(persona)
                        if controllo is not None:
                            if len(libreria) < 1:
                                print("Abbiamo esaurito i libri, torna più tardi!")
                                cancella_albero()
                            else:
                                while vedi_per_reparto() is False:
                                    print("Scaffale vuoto!")
                                    vedi_per_reparto()
                                raccogli_richiesta(persona)
                            semaforo = 1
                        else :
                            print("\nDati errati, riprova!\n ")
                            tentativi = tentativi + 1
                        if tentativi == 3:
                            print("Hai esaurito i tentativi!\n")
                            cancella_albero()
                            semaforo = 1

                elif albero.element(figlio6) == 2:
                    # -------------------------------------------------------------------MENU CLIENTE.ORDINE.ABBONATI(1,2)
                    decisione = menu_non_abbonati()
                    figlio14 = albero.add_left(figlio6, decisione)
                    if albero.element(figlio14) == 2:
                        nome = str(input("\nInserisci il tuo nome: "))
                        codice = random.randrange(10, 500, 1)
                        codice = str(codice)
                        print(
                            "\nTi è stato assegnato il codice: " + codice + " la tua richiesta sarà effettuata appena possibile!")

                        persona = nome + " " + codice
                        if len(libreria) < 1:
                            print("Abbiamo esaurito i libri, torna più tardi!")
                            cancella_albero()
                        else:
                            while vedi_per_reparto() is False:
                                print("Scaffale vuoto!")
                                vedi_per_reparto()
                            raccogli_richiesta(persona)

                    elif albero.element(figlio14) == 1:
                        # -------------------------------------------------------------------MENU CLIENTE.ORDINE.ABBONATI.TIPOABBONAMENTO(1,2)
                        decisione = menu_tipo_abbonamento()
                        figlio19 = albero.add_left(figlio14, decisione)
                        if albero.element(figlio19) == 1:
                            nome = str(input("\nInserisci il tuo nome: "))
                            codice = random.randrange(1, 50, 1)
                            codice = str(codice)
                            persona = nome + " " + codice
                            inserimento_gold(persona, riferimento)
                            save_obj(utenti, "Lista_utenti")
                            print("\nTi è stato assegnato il codice: " + codice + " le tue richieste saranno le prime ad essere gestite!")
                            if len(libreria) < 1:
                                print("Abbiamo esaurito i libri, torna più tardi!")
                                cancella_albero()
                            else:
                                while vedi_per_reparto() is False:
                                    print("Scaffale vuoto!")
                                    vedi_per_reparto()
                                raccogli_richiesta(persona)
                        elif albero.element(figlio19) == 2:
                            nome = str(input("\nInserisci il tuo nome: "))
                            codice = random.randrange(50, 100, 1)
                            codice = str(codice)
                            persona = nome + " " + codice
                            inserimento_silver(persona, riferimento)
                            save_obj(utenti, "Lista_utenti")
                            print("\nTi è stato assegnato il codice: " + codice + " le tue richieste saranno gestite con priorità superiore alla media!")
                            if len(libreria) < 1:
                                print("Abbiamo esaurito i libri, torna più tardi!")
                                cancella_albero()
                            else:
                                while vedi_per_reparto() is False:
                                    print("Scaffale vuoto!")
                                    vedi_per_reparto()
                                raccogli_richiesta(persona)
