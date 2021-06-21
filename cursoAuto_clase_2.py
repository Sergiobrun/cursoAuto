# programa de promedios

def promedio(matematica, literatura, fisica):
    prom = (matematica + literatura + fisica)/3
    return prom

def imprimir(nombres,apellidos, promedioss ):
    print(nombres+' '+apellidos+' promedio '+str(promedioss()))

def calificar(average):
    if average()>=6:
        print('aprobado')
        if average()>9:
            print('alumno destacado')
    elif average()<4:
        print('insuficiente')
    else:
        print('a recuperatorio')

nombre = input('nombre ')
apellido = input('apellido ')
matematica = int(input('mat '))
literatura = int(input('lit '))
fisica = int(input('fis '))

prome = promedio(matematica, literatura, fisica)
imprimir(nombre, apellido, prome)
calificar(prome)