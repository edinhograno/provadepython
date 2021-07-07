from Livros import Livro
from Autor import Autor
from Pilha import Pilha

pilha = Pilha()

pilha.adiciona(1, "Harry Quatro Oio", Autor(10, "Sem pai"))
pilha.adiciona(2, "Branca de Neve", Autor(11, "Sony Pictures"))
pilha.adiciona(3, "Chapeuzinho Vermeio", Autor(12, "Playstation"))
pilha.adiciona(4, "Bacana é todo mundo", Autor(13, "PC da Hora"))

print(pilha.imprimir())

# SOR SE QUISER DELETAR FICA A VONTADE DESCOMENTA AI, É NOIS E ME DA UM AZÃO \o/
# pilha.remove()
# print(pilha.imprimir())

