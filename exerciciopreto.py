Algoritmo: Crescimento da Oliveira

var
   idade: inteiro
   altura: real

inicio

   escreva("Digite a idade da oliveira em anos: ")
   leia(idade)

   altura <- idade * 30

   escreva("Altura estimada: ", altura, " cm\n")

   se altura > 500 entao
      escreva("Oliveira adulta")
   senao
      escreva("Oliveira em crescimento")
   fimse

fim
