def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso (kg) e altura (m)."""
    if altura <= 0: 
        return "Altura deve ser maior que zero."
    return round (peso / (altura ** 2), 2)

def classificar_imc(imc):
    """Classifica o IMC conforme tabela da OMS."""
    if imc < 18.5: 
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25: 
        return "Peso normal"
    elif imc >= 25 and imc < 30: 
        return "Sobrepeso"
    elif imc >= 30 and imc < 35: 
        return "Obesidade grau I"
    elif imc >= 35 and imc < 40: 
        return "Obesidade grau II"
    else: 
        return "Obesidade grau III"