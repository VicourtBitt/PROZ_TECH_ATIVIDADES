const numerosDaSorte = [37, 14, 26, 5, 94, 87]

numerosDaSorte.forEach((numero) => {
    // forEach é um método que passa paraCadaNumero (tradução literal)
    // então, para cada numero dentro do array/lista, faça algo abaixo
  if (numero % 2 == 0 && numero < 50){
    console.log("Número é par e ainda é menor que 50")
  } else if (numero < 50) {
    console.log("Número é menor que 50")
  } else {
    console.log("Número é maior que 50")
  }
})