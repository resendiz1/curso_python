#Iniciando con las tuplas, son restrictivas 

nombreTupla = [1,6,5,6, 'Resendiz']
print(nombreTupla[3])

#convirtiendo un tupla en una lista
lista = list(nombreTupla)
lista.pop()
print(lista)

#convirtiendo una lista en una tupla
tupla = tuple(lista)
print(tupla)



#Verificando si hay elementos en una tupla
print('Resendiz' in nombreTupla)


#preguntando cuantas veces esta un elemento en la tupla count()
print(nombreTupla.count('Resendiz'))


#Preguntando la longitud de la tupla
print(len(nombreTupla))




#Declarando una tupla sin parentesis
tuplaINdividuo = ('Arturo',6, '1993')
nombre, dia, anio = tuplaINdividuo

print(tuplaINdividuo)
print(nombre)


print('\n \n \n')
