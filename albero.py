class Tree:
    """
    Classe base astratta che rappresenta una struttura ad albero
    """

#----------------- Classe Position Innestata
    class Position:
        """
        Un astrazione che rappresenta la posizione di un singolo elemento
        """
        def element(self):
            """
            Restituisce l'elemento memorizzato in questa Position
            :return:
            """
            raise NotImplementedError("Deve essere implementato dalla sottoclasse")

        def __eq__(self, other):
            """
            Restituisce True se 'other' rappresenta la stessa posizione
            :param other:
            :return:
            """
            raise NotImplementedError("Deve essere implementato dalla sottoclasse")

        def __ne__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione
            :param other:
            :return:
            """
            return not(self == other)  # opposto a _eq__

        def __iter__(self):
            """
            Restituisce un iteratore che scandisce tutti gli elementi dell'albero
            :return:
            """
            for p in self.positions():
                yield p.element()

#----metodi astratti che la sottoclasse concreta deve supportare
    def root(self):
        """
        Restituisce Position che rappresenta la radice dell'albero
        :param self:
        :return:
        """
        raise NotImplementedError("Deve essere implementato dalla sottoclasse")

    def parent(self, p):
        """
        Restituisce Position che rappresenta il genitore di 'p'
        None se 'p' è radice
        :param self:
        :param p:
        :return:
        """
        raise NotImplementedError("Deve essere implementato dalla sottoclasse")

    def num_children(self, p):
        """
        Restituisce il numero di figli della Position 'p'
        :param self:
        :param p:
        :return:
        """
        raise NotImplementedError("Deve essere implementato dalla sottoclasse")

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'
        :param self:
        :param p:
        :return:
        """
        raise NotImplementedError("Deve essere implementato dalla sottoclasse")

    def __len__(self, p):
        """
        Restituisce True se la Position 'p' non ha figli
        :param self:
        :param p:
        :return:
        """
        return self.num_children(p) == 0
    def is_root(self,p):
        """
        Restituisce True se la postion 'p' è la radice dell albero
        :param self:
        :param p:
        :return:
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Restituisce True se la Postion 'p' non ha figli
        :param self:
        :param p:
        :return:
        """
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """
        Restituisce il numero di livelli che separano la position 'p' dalla radice
        :param self:
        :param p:
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _heigh2(self, p):
        """
        Restituisce l'altezza del sottoalbero radicato in Position 'p'
        :param self:
        :param p:
        :return:
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._heigh2(c) for c in self.children(p))

    def heigh(self, p = None):
        """
        Restituisce l'altezza del sottoalbero radicato in Position 'p'
        Se 'p' è None restituisce l'altezza dell'intero albero
        :param self:
        :param p:
        :return:
        """
        if p is None:
            p = self.root()
        return self._heigh2(p)

    #--Attraversamento pre-ordine
    def preorder(self):
        """
        Genera un iterazione preordinata delle posizioni nell'albero
        :param self:
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  #Inizia la ricorsione
                yield p

    def _subtree_preorder(self, p):
        """
        Genera un iterazione preordinata delle posizoni nel
        sottoabero con radice 'p'
        :param self:
        :param p:
        :return:
        """
        yield p                             #Visita 'p' prima dei suoi sotto alberi
        for c in self.children(p):          #per ogni figlio di c
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        """
        Restituisce un contenitore iterabile con tutte le posizioni dell'albero
        :param self:
        :return:
        """
        return self.preorder()

    # ----Attraversamento post-ordine
    def postorder(self):
        """
        Genera un iterazione postordinata delle poszioni nell'albero
        :param self:
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()): #Inizia la ricorsione
                yield p

    def _subtree_postorder(self, p):
        """
        Genera un ietrazione postordinata delle posizioni nel sottoalbero con radice 'p'
        :param self:
        :param p:
        :return:
        """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

