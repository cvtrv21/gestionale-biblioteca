from AlberoBinario import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """
    Rappresentazione concatenata di una struttura ad albero binario
    """

    class _Node:
        """
        Classe leggera, non pubblica per la memorizzazione di un nodo
        """

        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right = None):
            """
            Costruttore
            :param element:
            :param parent:
            :param left:
            :param right:
            """
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        #-------------------------
    class Position(BinaryTree.Position):
        """
        Astrazione che rappresenta la posizione di un singolo elemento
        """

        def __init__(self, container, node):
            """
            Costruttore
            :param container:
            :param node:
            """
            self._container = container
            self._node = node

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa Position
            :return:
            """
            return self._node._element

        def __eq__(self, other):
            """
            Restituisce True se 'other' Position rappresenta la stessa posizione
            :param other:
            :return:
            """
            return type(other) is type(self) and other._node is self._node

        #-----------------------------------------

    def _validate(self, p):
        """
        Restituisce il nodo associato, se la posizione è valida
        :param p:
        :return:
        """
        if not isinstance(p, self.Position):
            raise TypeError('p deve essere di tipo Position')
        if p._container is not self:
            raise ValueError('p non appartiene a questo contenitore')
        if p._node._parent is p._node:
            raise ValueError('p non è più valido')
        return p._node

    def _make_position(self, node):
        """
        Restituisce l'istanza Position per il nodo dato
        None se nessun NODO
        :param node:
        :return:
        """
        return self.Position(self, node) if node is not None else None

    #-------COSTRUTTORE ALBERO BINARIO---
    def __init__(self):
        """
        Crea un albero binario inizialmente vuoto
        """
        self._root = None
        self._size = 0

    #------metodi accessori
    def __len__(self):
        """
        Restituisce il numero totale di elementi nell'albero
        :return:
        """
        return self._size()

    def root(self):
        """
        Restituisce Position che rappresenta la radice dell'albero
        None se è vuoto
        :return:
        """
        return self._make_position(self._root)

    def parent(self, p):
        """
        Restituisce Postion che rappresenta il genitore di 'p'
        None se è la radice
        :param p:
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """
        Restituisce una Position che rappresenta il figlio sinistro di 'p'
        None se non ha figlio sinistro
        :param p:
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """
        Restituisce una Position che rappresenta il figlio destro di 'p'
        None se non ha figlio destro
        :param p:
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """
        Restituisce il numero di figli della Postion 'p'
        :param p:
        :return:
        """
        node = self._validate(p)
        count = 0
        if node._left is not None:   #Il figlio sinistro esiste
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """
        Posizione l'elemento 'e' alla radice di un albero
        ValueError se l'albero non è vuoto
        :param e:
        :return:
        """
        if self._root is not None:
            self._root = self._Node(e)
            return self._make_position(self._root)
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """
        Crea un nuovo figlio sinistro per la Position 'p' memorizzado l'elemento 'e'
        Retituisce la Postion del nuovo Nodo
        :param p:
        :param e:
        :return:
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Il figlio sinistro gia esiste')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        """
        Crea un nuovo figlio destro per la Postion 'p' memorizzando l'elemento 'e'
        Restituisce la Position del nuovo nodo
        :param p:
        :param e:
        :return:
        """

        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Il figlio destro esiste già")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        """
        Sostituisce l'elemento in posizione 'p' con 'e'
        :param p:
        :param e:
        :return:
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """
        Elimina il nodo in Position 'p' e lo sostituisce con il figlio se presente

        Restituisce l'elemento che era stato memorizzato in quella Postion
        :param p:
        :return:
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("La posizione p ha 2 figli")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._left = child
        self._size -= 1
        node._parent = node
        return node._element

    def attach(self, p, t1, t2):
        """
        Collega gli alberi t1 e t2 come sottoalberi sinistro e destro della foglia p
        :param p:
        :param t1:
        :param t2:
        :return:
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("La posizione 'p' deve essere foglia")
        if not type(self) is type(t1) is type(t2):  # Tutti gli alberi devono essere dello stesso tipo
            raise TypeError("La tipologia di albero deve essere uguale")
        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def element(self, p):
        """
        Restituisce l'elemento memorizzato in questa Position
        :return:
        """
        return self.Position.element(p)
