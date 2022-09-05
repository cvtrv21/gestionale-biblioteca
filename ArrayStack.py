from empty import Empty

class ArrayStack:
    """
    Implementazione di una pila LIFO utilizzndo una lista python
    """

    def __init__(self):
        """
        Crea una pila vuota
        """
        self._data = [] # istanza della lista non pubblica


    def __len__(self):
        """
        Restituisce il numero di elementi nella pila
        """
        return len(self._data)


    def is_empty(self):
        """
        Restituisce True se la pila è vuota

        """
        return len(self._data) == 0


    def push(self, e):
        """
        Aggiunge un elemento 'e' in cima alla lista '
        """
        self._data.append(e)   # Nuovo elemento alla fine della lista


    def top(self):
        """
        Restituisce senza eliminare l'elemento in cima alla pila

        Solleva l'eccezione empty se la pila è vuota
        """
        if self.is_empty():
            raise Empty('La pila è vuota')
        return self._data[-1]  # ultimo elemento nella lista


    def pop(self):
        """
        Restituisce e rimuovere l'elemento in cima alla pila(LIFO)

        Solleva l'eccezione empty se la pila è vuota
        """
        if self.is_empty():
            raise Empty('La pila è vuota')
        return self._data.pop() # Rimuove l'ultimo elemento della lista