
def imprimir(a,b,c,d,e):
    print(a,b,c,d,e)

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
for i in range(5):            
    nombre = input('nombre: ')
    apellido = input('apellido: ')
    marca = input('marca: ')
    puertas_del_auto = input('puertas: ')
    color = input('color: ')

    precio = 0
    calc_precio_marca(marca)
    calc_precio_puertas(puertas_del_auto)
    imprimir(nombre, apellido, marca, puertas_del_auto, precio)
