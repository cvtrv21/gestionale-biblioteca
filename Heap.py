from empty import Empty
from coda_prio_base import PriorityQueueBase
class HeapPriorityQueue(PriorityQueueBase):
    """
    Coda con priorità min-oriented implementata con heap binario
    """

    #-----Metodi non pubblici----
    def _parent(self, j):
        return ( j - 1) // 2

    def _left(self, j):
        return 2 * j +1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        Sacambia gli elementi negli indici i e j dell'array
        :param i:
        :param j:
        :return:
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) #prosegue nella posizione del genitore

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  #Anche se la destra potrebbe ssere piu piccola
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    #------Metodi pubblici------
    def __init__(self):
        """
        Crea una coda prioritaria
        """
        self._data = []

    def __len__(self):
        """
        Restituisce il numero di elementi nella coda prioritaria
        :return:
        """
        return len(self._data)

    def add(self, key, value):
        """
        Aggiunge una coppia chiave-valore alla coda prioritaria
        :param key:
        :param value:
        :return:
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1) #Fa risalire la posizione aggiunta

    def min(self):
        """
        Restituisce ma non rimuove la tupla(k,v) con chiave minima.
        Solleva l'eccezione Empty se la cosa è vuota
        :return:
        """
        if self.is_empty():
            raise Empty("La coda prioritaria è vuota")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        Restituisce e rimuove la tupla(k,v) con chiave minima
        :return:
        """
        if self.is_empty():
            raise Empty("La coda prioritaria è vuota")
        self._swap(0, len(self._data) - 1) #mette l'elemnto più piccolo alla fine
        item = self._data.pop()            #elimina l'elemento dalla lista
        self._downheap(0)
        return (item._key, item._value)
