const conta = (value1, value2, op) => {
    let response = null
    let template = `${value1} ${op} ${value2}`
    switch (op){
        case "*":
            response = value1 * value2
            return `${template} = ${response}`
        
        case "+":
            response = value1 + value2
            return `${template} = ${response}`

        case "-":
            response = value1 - value2
            return `${template} = ${response}`

        case "/":
            response = value1 / value2
            return `${template} = ${response}`
            
        default:
            template = "O operador informado não é válido"
            return template
    }
}

console.log(conta(4, 5, "+"))
console.log(conta(4, 5, "-"))
console.log(conta(4, 5, "*"))
console.log(conta(4, 5, "/"))