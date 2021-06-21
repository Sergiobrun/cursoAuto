
lista_de_marcas = ['chevrolet', 'ford', 'fiat']
lista_de_cant_puertas = ['2','4','5']
lista_de_respuestas = ['Si', 'No']
lista_de_pedidos = []

def calc_precio_marca(marca):
    global precio
    if marca == 'chevrolet':
        precio = precio + 120000
    elif marca == 'ford':
        precio = precio + 100000
    elif marca == 'fiat':
        precio = precio + 80000
    else:
        print('esa marca no se vende aca')

def calc_precio_puertas(puertas):
    global precio 
    if precio != 0:
        if puertas == '2':
            precio = precio + 50000
        if puertas == '4':
            precio = precio + 65000
        if puertas == '5':
            precio = precio + 78000
        else:
            print('no tenemos autos con esa cantidad de puertas')


#preguntas

mas_pedidos = 'Si'

while mas_pedidos == 'Si':
    pedido = {}
    pedido['nombre'] = input('nombre: ')
    pedido['apellido'] = input('apellido: ')

    pedido['marca'] = input('marca: ')
    while pedido['marca'] not in lista_de_marcas:
        pedido['marca'] = input('pone de nuevo la marca: ')

    pedido['puertas'] = input('puertas: ')
    while pedido['puertas'] not in lista_de_cant_puertas:
        pedido['puertas'] = input('pone de nuevo la cantidad de puertas: ')

    precio = 0
    calc_precio_marca(pedido['marca'])
    calc_precio_puertas(pedido['puertas'])
    pedido['precio'] = precio

    lista_de_pedidos.append(pedido)
    mas_pedidos = input('va a haber otro pedido? (Si/No) ')
    while mas_pedidos not in lista_de_respuestas:
        mas_pedidos = input('responde  bien gato: ')

if len(lista_de_pedidos) > 50:
    for i in lista_de_pedidos:
        i['precio'] = i['precio'] * 0.82 
elif len(lista_de_pedidos) > 10:
    for i in lista_de_pedidos:
        i['precio'] = i['precio'] * 0.85
elif len(lista_de_pedidos) > 5:
    for i in lista_de_pedidos:
        i['precio'] = i['precio'] * 0.9

print(lista_de_pedidos)
