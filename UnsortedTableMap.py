from MapBase import MapBase

class UnsortedTableMap(MapBase):
    """
    Implementazione della mappa utilizzando una lista non ordinata
    """

    def __init__(self):
        """
        Crea una mappa vuota
        """
        self._table = []  #lista di _Item

    def __getitem__(self, k):
        """
        Restituisce il valore associato alla chiave 'k'

        Solleva un KeyError se non trovato
        :param k:
        :return:
        """
        for item in self._table:
             if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))  #repr(): restituisce stringa

    def __setitem__(self, k, v):
        """
        Assegna il valore 'v' alla chiave 'k', sovrascrivendo il valore
        esistente se presente
        :param k:
        :param v:
        :return:
        """
        for item in self._table:
            if k == item._key:   #Se trova la chiave
                item._value = v  #Sovrascrive il valore
                return           #esce
        #Se non trova la chiave
        self._table.append(self._Item(k, v))


    def __delitem__(self, k):
        """
        Rimuove l'elemento associato alla chiave 'k'
        Solleva un keyError se non trovato
        :param k:
        :return:
        """
        for j in range (len(self._table)):
           if k == self._table[j]._key: #se trova la chiave
                self._table.pop(j)      #rimuove l'elemento
                return                  #esce
        raise KeyError('KeyError: ' + repr(k))

    def __isKey__(self, k):
        for item in self._table:
            if k == item._key:  #Se trova la chiave
                return True


    def __len__(self):
        """
        Restituisce il numero di elementi nella mappa
        :return:
        """
        return len(self._table)

    def __iter__(self):
        """
        Genera iterazione delle chiavi della mappa
        :return:
        """
        for item in self._table:
            yield item._key
