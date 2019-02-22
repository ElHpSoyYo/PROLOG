def mi_funcion():
    edades=[26,28,65,23,56]
    mayoresEdad = edades
    
    copia1Edades = edades[:]
    copia2Edades = list(edades)
    
    print("Inicial:\t", edades)
    print("Referencia:\t", mayoresEdad)
    print("Copia 1: \t", copia1Edades)
    print("Copia 2:\t", copia2Edades)
    print("-----------------Asignaciones-------------")
    mayoresEdad[0:2]= [40,80]
    copia1Edades[0:2] = [50,90]
    copia2Edades[0:2]= [30,70]
    
    print("\"Original\":\t",edades)
    print("Referencia:\t", mayoresEdad)
    print("Copia 1:\t", copia1Edades)
    print("Copia 2:\t", copia2Edades)
    
if __name__ =='__main__':
    mi_funcion()
