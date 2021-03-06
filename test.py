from calculadoraLib import suma, resta, multiplicacion, division, raiz

def test_suma():
	#arrange
	vectordata=[[1,5,7],[6,3,5],[3,-1,2]]
	vectorespuesta=[]
	#act
	for n,v in enumerate(vectordata):
		vectorespuesta.append(suma(v[0],v[1]))
		#assert
		if v[2]==vectorespuesta[n]:
			print("La funcion suma es correcta: ",v[0]," + ", v[1]," =",vectorespuesta[n])
		else:
			print("Error de la funcion suma deberia ser ",v[0]," + ",v[1]," = ",vectorespuesta[n],"pero se tiene almacenado ",v[2])

def test_resta():
        #arrange
    vectordata=[[5,3,2],[6,3,3],[3,-1,4]]
    vectorespuesta=[]
    #act
    for n,v in enumerate(vectordata):
        vectorespuesta.append(resta(v[0],v[1]))
    #assert
        if v[2]==vectorespuesta[n]:
            print("La funcion resta es correcta: ",v[0]," + ", v[1]," =",vectorespuesta[n])
        else:
            print("Error de la funcion resta deberia ser ",v[0]," + ",v[1]," = ",vectorespuesta[n],"pero se tiene almacenado ",v[2])

def test_multiplicacion():
        #arrange
    vectordata=[[1,5,5],[6,3,18],[3,1,3]]
    vectorespuesta=[]
    #act
    for n,v in enumerate(vectordata):
        vectorespuesta.append(multiplicacion(v[0],v[1]))
    #assert
        if v[2]==vectorespuesta[n]:
            print("La funcion multiplicacion es correcta: ",v[0]," + ", v[1]," =",vectorespuesta[n])
        else:
            print("Error de la funcion multiplicacion deberia ser ",v[0]," + ",v[1]," = ",vectorespuesta[n],"pero se tiene almacenado ",v[2])

def test_division():
        #arrange
    vectordata=[[10,5,2],[6,3,2],[3,1,3]]
    vectorespuesta=[]
    #act
    for n,v in enumerate(vectordata):
        vectorespuesta.append(division(v[0],v[1]))
    #assert
        if v[2]==vectorespuesta[n]:
            print("La funcion division es correcta: ",v[0]," + ", v[1]," =",vectorespuesta[n])
        else:
            print("Error de la funcion division deberia ser ",v[0]," + ",v[1]," = ",vectorespuesta[n],"pero se tiene almacenado ",v[2])

def test_raiz():
    #arrange
    vectordata=[[9,3],[16,4],[25,5]]
    vectorespuesta=[]
    #act
    for n,v in enumerate(vectordata):
        vectorespuesta.append(raiz(v[0]))
    #assert
        if v[1]==vectorespuesta[n]:
            print("La funcion raiz es correcta: ",v[0]," = ",vectorespuesta[n])
        else:
            print("Error de la funcion division deberia ser ",v[0]," = ",vectorespuesta[n],"pero se tiene almacenado ",v[2])


if __name__ == '__main__':
	opcion="S"
	while opcion=="S" or opcion=="s":
		print("**** TEST DE MI CALCULADORA****")
		print("1: Suma")
		print("2: Resta")
		print("3: Multiplicacion")
		print("4: Division")  
		print("5: Raiz")  
		opcion=int(input("Selecione una opcion: "))
		if opcion==1:
			test_suma()
		elif opcion==2:
			test_resta()
		elif opcion==3:
			test_multiplicacion()
		elif opcion==4:
			test_division()
		elif opcion==5:
			test_raiz()
		opcion=input("Desea continuar S/N: ")
	print("Se realizado los test de operaciones basicas")
