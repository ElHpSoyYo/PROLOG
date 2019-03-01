# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:18:53 2019

@author: Esteban Palacio Londoño C.C: 1017269600
"""
import re
miPatron1= re.compile(r'\btres\b')

texto= """CALLE 64 A No. 94- 62- BR ROBLEDO LA CAMPIÑA
Kr 59A No. 89 C- 150- BRR EL PARAISO
CALLE 22 No. 70A- 32- BARRIO BELEN SAN BERNARDO
Cll 109 No. 50- 13- BARRIO ANDALUCIA LA FRANCIA - APT- 205
CALLE 102 # 64- 68- APTO 201- BARRIO BELALCAZAR
Carrera 59 No. 65- 140- BARRIO LA IGUANA- APTO- 30"""

patronCalle = re.compile(r'\bCALLE|Cll\b')
texto2= patronCalle.sub("Calle",texto)
patronCarrera = re.compile(r'\bKr\b')
texto3= patronCarrera.sub("Carrera",texto2)
patronNum= re.compile(r'\bNo.')
texto4=patronNum.sub("#",texto3)
patronBar= re.compile(r'\bBRR|BARRIO|BR\b')
texto5=patronBar.sub("Barrio", texto4)

L= texto5.split('\n')
for i in L:
    a= i.split(' ')
    primero = a[4]
    segundo= a[5]
    if not (primero[-1].isalpha()):
        print(primero)


"""
print("Uso de split - separarar por 'tres'")
print(miPatron1.split(texto))

print("Uso de split- separar por  palabras que empiecen por mayuscula")
miPatron2= re.compile(r'\b[A-Z]\w*\b')
print(miPatron2.split(texto))

print("Uso de Sub - Cambiar Triste por Alegre")
miPatron3= re.compile(r'\b(T|t)riste')
texto2 = miPatron3.sub("Alegre",texto)
print(texto2)

print("Extraer todas las palabara que comniences por Tr o tr")
print(re.findall(r'\b[T|t]r\w*',texto))
"""
