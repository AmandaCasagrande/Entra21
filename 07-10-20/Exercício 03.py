#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

cabecalho = """\n\n\nAs crianças são pequenos cientistas

Como já dizia um dos mais importantes pesquisadores de educação e pedagogia, Jean
Piaget: as crianças são pequenos cientistas. Essa frase faz todo o sentido para quem convive
com os pequenos. Eles tentam explorar o mundo a todo o momento, por vezes com o corpo
todo, de modo a experimentar, testar, conhecer ecompreender tudo que os cerca.
A curiosidade os guia por caminhos diversos e chega um momento em que já não basta
conhecer, eles querem também entender a origem e o funcionamento das coisas.

Assim, além de pequenos cientistas, também são pequenos filósofos, que todos os dias
repensam aquilo que já conhecem, descobrindo novos mundos e questionando o que já
sabem. Nesse processo, os adultos não saem ilesos. Na tentativa, muitas vezes engraçada e
embaraçosa, de responder os “porquês” das crianças, nós também acabamos repensando
nossos conceitos já estabelecidos. Aqueles mais empolgados podem ainda ajudar a criança a
problematizar e a ir mais longe em seus questionamentos, estimulando seu pensamento
crítico e filosófico ao invés de responder rapidamente, resolvendo seus “porquês”."""

print(cabecalho.format())
print("\n\n\nInformações sobre a publicação: ")
tituloPublic = "As crianças são pequenos cientistas"
print("\n\nTítulo: {}".format(tituloPublic))

edicaoPublic = "1ª Edição, Editora SM"
print("\nEdição: {}".format(edicaoPublic))

autorPublic = "Laurent Moreau"
print("\nAutor(a): {}".format(autorPublic))

dataPublic = "2015"
print("\nData de publicação: {}".format(dataPublic))
