from Livros import Livro

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def adiciona(self, id, nome, autor):
        node = Livro(id, nome, autor)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def remove(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.titulo
        raise IndexError("A pilha está vazia")

    def imprimir(self):
        linha = "========="
        hook = ""
        pointer = self.top
        while(pointer):
            hook = hook + str(f" \n Id: {pointer.id} \n Titulo: {pointer.titulo} \n Autor: {pointer.autor.nome}\n {linha}") + "\n"
            pointer = pointer.next
        return hook