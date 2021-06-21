
lista_de_marcas = ['chevrolet', 'ford', 'fiat']
lista_de_cant_puertas = ['2','4','5']
lista_de_respuestas = ['Si', 'No']
lista_de_pedidos = []

def calc_precio(marca, puertas):
    marcas = {'ford': 100000, 'chevrolet': 120000, 'fiat':80000}
    puertas_a_elegir = {'2': 5000, '4':15000, '5':20000}
    precio = marcas[marca] + puertas_a_elegir[puertas] 
    return precio


#preguntas que van a hacersele al cliente

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

    pedido['precio'] = calc_precio(pedido['marca'], pedido['puertas'])

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
