from eficiencia_motor import *

def test_calcular_eficiencia():
    assert calcular_eficiencia(900,1000) == 90
    assert calcular_eficiencia(855,1000) == 85.5
    assert calcular_eficiencia(1000,0) == "Potência de entrada deve ser maior que zero." 

def test_classificar_eficiencia():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa eficiência"
    assert classificar_eficiencia(85.0) == "IE2 Eficiência média"
    assert classificar_eficiencia(92.0) == "IE3 Alta eficiência"

def test_analise_motor():
    assert analise_motor(880,1000) == {
        "potencia_saida": 880,
        "potencia_entrada": 1000,
        "eficiencia": 88.0,
        "classificacao": "IE2 Eficiência média",
    }