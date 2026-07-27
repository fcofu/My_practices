for numero in range(2, 20, 3):
    numero = numero + 1
    print(numero)


el_diccionario = {
    'ramon' : 'naranja',
    'pedro' : 'rojo',
    'ricardo' : 'azul',
    'laura' : 'rosa'
}
for olag in el_diccionario.values():
    print(olag + "wande")


segundo_dic = {
    'blanca' : '125',
    'cafe' : '49',
    'azul' : '311',
    'naranja' : '11'
}

for (numero,(color_casa, direccion_casa)) in enumerate(segundo_dic.items(),1):
    print(f" Casa {numero}. {color_casa} {direccion_casa}")
