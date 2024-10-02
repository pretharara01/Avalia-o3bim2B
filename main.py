elementos = {
    "H": {"nome": "Hidrogênio", "numero_atomico": 1},
    "He": {"nome": "Hélio", "numero_atomico": 2},
    "Li": {"nome": "Lítio", "numero_atomico": 3},
}

def consultar_elemento(sigla):
    sigla = sigla.upper()
    if sigla in elementos:
        return elementos[sigla]
    else:
        return "Elemento não encontrado, tente novamente."

def obter_input():
    elementos = input("Digite a sigla do elemento: ")
    return elementos

print(consultar_elemento(obter_input()))