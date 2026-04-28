algoritmo "irrigacao"

var
   agua, ciclos: inteiro

inicio

   agua <- 500
   ciclos <- 0

   enquanto agua >= 30 faca

      agua <- agua - 30
      ciclos <- ciclos + 1

      escreva("Água restante: ", agua, " litros\n")

   fimenquanto

   escreva("\nTotal de ciclos realizados: ", ciclos)

fimalgoritmo
