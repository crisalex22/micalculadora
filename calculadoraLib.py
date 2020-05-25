def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def multiplicacion(a,b):
	return a*b

def division(a,b):
		return a/b
def raiz(s): 
    pSq = 0;  
    N = 0;  
    for i in range(int(s), 0, -1): 
        for j in range(1, i): 
            if (j * j == i): 
                pSq = i; 
                N = j; 
                break; 
      
        if (pSq > 0): 
            break; 
  
    d = s - pSq;     # calculate d 
    P = d / (2.0 * N); # calculate P 
    A = N + P; # calculate A 
    # calculate sqrt(S). 
    sqrt_of_s = A - ((P * P) / (2.0 * A));  
    return sqrt_of_s; 

