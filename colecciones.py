#colecciones

# listas -> conjunto ordenado de elementos
lista = ['asd','asdf','ert']
print(lista[-2])
lista.append('fdgh')
lista.insert(1, 'pancha')
del lista[0]
print(len(lista))
lista[1] = 'linda'
print(lista)

# tuplas -> colecciones ordenadas inmutables, creo una y no la puedo modificar
lista_tupla = ('asd','dfg')
print(lista_tupla[1])

# diccionarios -> listas no ordenadas con par clave de valor, hay un key y un value
usuario = {'id': 1, 'name':'pedro', 'age':37, 'casado': True}
print(usuario['age'])
del usuario['casado']
print(usuario)
print(usuario.keys())
print(usuario.values())

