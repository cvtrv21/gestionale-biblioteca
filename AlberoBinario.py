from albero import Tree

class BinaryTree(Tree):
    """
    Classe Astratta che rappresenta una struttura ad albero Binario
    """
    def left(self, p):
        """
        Restituisce una Postion che rappresenta il figlio sinistro di 'p'
        Restituisce None se 'p' non ha figlio sinistro
        :param p:
        :return:
        """
        raise NotImplementedError("Deve essere imlementato nella sottoclasse")

    def right(self, p):
        """
        Restituisce una Position che rappresenta il figlio destro di 'p'
        Restituisce None se 'p' non ha figlio destro
        :param p:
        :return:
        """

        #---metodi concreti implementati in questa classe
    def sibling(self, p):
        """
        Restituisce una Position che rappresenta il fratello di 'p'
        None se non ha fratello
        :param p:
        :return:
        """
        parent = self.parent(p)
        if parent is None:  # allora 'p' è radice
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)  #Possibilmente None
            else:
                return self.left(parent)

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli di posizione 'p'
        :param p:
        :return:
        """
        if self.left(p) is not None:
            yeld.self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
