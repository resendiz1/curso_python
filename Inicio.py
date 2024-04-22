def mensaje(a,b):
    resultado = a*b
    return resultado


resultado = mensaje(1,3)

#print(mensaje(10,20))
#print(resultado)

print('  ************* LISTAS O ARREGLOS ************* \n')
        #Arreglos o listas 

#sintaxis
nombreLista = ['elemento 1', 20, 'elemento 2', True, False, 1, 65 ]


#agregando elementos al final de la lista con append()
nombreLista.append('Elemento agregado con append')


#agregando elemento en cualquier posicion de la lista con insert(posicion, elemento)
nombreLista.insert(2, 'Elemento agregado en la popsicion 2')


#agregando varios elementos a la lista con extend()
nombreLista.extend(['extend 1', 'extend 2', 2, 656])



print('imprime el elemento con la posición 2 del arreglo')
#imprime el elemento con la posición 2 del arreglo
print(nombreLista.index(2))
print('\n \n')

#preguntar si un elemento se encuentra en la lista 
print('preguntar si un elemento se encuentra en la lista')
respuesta = 255 in nombreLista
print(respuesta)
print('\n \n')


#remueve el elemento que le digas remove(elemento_a_eliminar)
print('remueve el elemento que le digas remove(elemento_a_eliminar)')
nombreLista.remove('extend 1')
print(nombreLista)
print('\n \n')



#remueve el ultimo elemento de una lista
print('remueve el ultimo elemento de una lista')
nombreLista.pop()
print(nombreLista)
print('\n \n')




#Declarando otra lista
lista2 = ['elemento lista 2', 'elemento 2 lista 2']


#Se unen concatenando las listas
lista3 = nombreLista + lista2
print(lista3*3)




#Salto de linea para no ver la consola hasta abajo
print('\n \n \n \n \n')


