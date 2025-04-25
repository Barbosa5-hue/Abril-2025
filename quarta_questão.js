var num01 = 9
var num02 = 4
var num03 = 6

function numero_maior(){
    if (num01 > num02 || num01 > num03){
        console.log(num01)
    }
    else if (num02 > num01 || num02 > num03){
        console.log(num02)
    }
    else if (num03 > num01 || num03 > num02){
        console.log(num03)
    }
    else{
        console.log("Todos são iguais")
    }
}
console.log(numero_maior())