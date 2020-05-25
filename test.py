from calculadoraLib import suma

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


if __name__ == '__main__':
	test_suma()