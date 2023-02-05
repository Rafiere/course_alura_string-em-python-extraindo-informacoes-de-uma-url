url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]

# Quando não inserimos um valor após o ":", ele pega todos os valores após o delimitador.
url_parametros = url[indice_interrogacao + 1:]

# Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == - 1:
    valor = url_parametros[indice_valor:indice_e_comercial]
else:
    valor = url_parametros[indice_valor: indice_e_comercial]

print(url_base)
print(url_parametros)
print(indice_parametro)
print(indice_valor)
print(valor)
