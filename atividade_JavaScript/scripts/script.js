const body = document.querySelector("body")
body.setAttribute("style", "margin: 0px; padding: 0px;")

const header = document.createElement("header")
header.setAttribute("style", "display: flex;height: 100px; width: 100%; background: #000")

const main = document.createElement("main")
main.setAttribute("style", "display: flex; height: 100%; width: 100%; justify-content: center; padding: 0.5em; box-sizing: border-box")

const card = document.createElement("div")
card.setAttribute("style", "display: flex; flex-direction: column; height: 360px; width: 480px; background: #CCCCCC; justify-content: space-around; align-items: center")

const productToSell = [
    {
        nome: "Garrafa Térmica",
        preco: 24.99,
        descricao: "Uma garrafa térmica para manter a temperatura da sua bebida"
    },
    {
        nome: "Televisão 32pol SMART",
        preco: 1299.99,
        descricao: "Ume televisão perfeita para você e para sua familia assistirem seus programas favoritos."
    }
]

const h2 = document.createElement("h2")
h2.textContent = productToSell[0].nome

const span = document.createElement("span")
span.textContent = `R$${productToSell[0].preco}`

const description = document.createElement("span")
description.textContent = productToSell[0].descricao

card.append(h2, span, description)
main.append(card)

const elementList = [header, main]

window.addEventListener("load", () => {
    elementList.forEach((elem) => {
        body.append(elem)
    })
})
