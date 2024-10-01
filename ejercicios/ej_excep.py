import math
import random


#1
n = float(input())
try:
    print(math.sqrt(n))
except ValueError:
    print("Tiene que ser un caracter numerico")
except:
    print("Ha ocurrido un error")

    
#2
lista = []
n = int(input())
while n != -1:
    lista.append(n)
    n = int(input())

error = 0
while error != 3:
    buscar = int(input("numero a buscar "))
    try:
        pos = lista.index(buscar)
        print(f"El numero esta en la posicion {pos+1}")
    except ValueError:
        print("No se encontro el numero")
        error += 1
    except:
        print("Ha ocurrido un error")
print(lista)


#3
num_azar = random.randint(1,500)
intento = 0
try:
    adivinar= int(input())
    intento += 1
    assert(adivinar > 1),"Numeros entre 1 y 500, se te suma un intento"
    assert(adivinar < 501),"Numeros entre 1 y 500, se te suma un intento"
except ValueError:
    print("Solo numeros, se te suma un intento")
    intento += 1
except AssertionError as error:
    print(error)
except:
    print("Ha ocurrido un error")
while adivinar != num_azar:
    if adivinar > num_azar:
        print(f"El numero es menor que {adivinar}, intento Nro: {intento}")
    else:
        print(f"El numero es mayor que {adivinar}, intento Nro: {intento}")
    try:
        adivinar= int(input())
        intento += 1
        assert(adivinar > 1),"Numeros entre 1 y 500, se te suma un intento"
        assert(adivinar < 501),"Numeros entre 1 y 500, se te suma un intento"
    except ValueError:
        print("Solo numeros, se te suma un intento")
        intento += 1
    except AssertionError as error:
        print(error)
    except:
        print("Ha ocurrido un error")
print(f"Adivinaste el numero en {intento} intentos") 

