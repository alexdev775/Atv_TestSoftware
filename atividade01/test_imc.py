from imc import *
def test_calcular():
    assert calcular_imc(70,1.75) == 22.86
    assert len(str(calcular_imc(70,1.75)).split(".")[1]) == 2
    assert calcular_imc(70,0) == "Altura deve ser maior que zero."
    

def test_classificar_imc():
    assert classificar_imc(17.9) == "Abaixo do peso"
    assert classificar_imc(22.0) == "Peso normal"
    assert classificar_imc(27.3) == "Sobrepeso"
    assert classificar_imc(33.0) == "Obesidade grau I"
    assert classificar_imc(37.0) == "Obesidade grau II"
    assert classificar_imc(45.0) == "Obesidade grau III"
