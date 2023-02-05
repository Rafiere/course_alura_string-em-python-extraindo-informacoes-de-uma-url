url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

indice_interrogacao = url.find('?')
url_base = url[0: indice_interrogacao]
# Quando não inserimos um valor após o ":", ele pega todos os valores após o delimitador.
url_parametros = url[indice_interrogacao + 1:]

print(url_base)
print(url_parametros)